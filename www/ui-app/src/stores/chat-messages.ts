import {SSE} from 'sse.js';
import {get, writable} from 'svelte/store';
import {PUBLIC_BOT_CHAT_API_URL} from '$env/static/public';

export interface ChatTranscript {
    messages: [{ '' }];
    chatState: 'idle' | 'loading' | 'error' | 'message';
}

const {subscribe, update, ...store} = writable<ChatTranscript>({
    messages: [
        {role: 'assistant', content: 'Hello, I am your virtual assistant. How can I help you?'}
    ],
    chatState: 'idle'
});

const set = async (query: string) => {
    updateMessages(query, 'user', 'loading');

    // const eventSource = new SSE('/api/chat', {
    //   headers: {
    //     'Content-Type': 'application/json'
    //   },
    //   payload: JSON.stringify({ messages: get(chatMessages).messages })
    // });
    //
    // eventSource.addEventListener('error', handleError);
    // eventSource.addEventListener('message', streamMessage);
    // eventSource.stream();

    const requestBody = {
        prompt : query
    }

    const chatResponse = await fetch(`${PUBLIC_BOT_CHAT_API_URL}/api/v1/chat/completions`, {
        headers: {
            'Content-Type': 'application/json'
        },
        method: 'POST',
        body: JSON.stringify(requestBody)
    });

    if (!chatResponse.ok) {
        const err = await chatResponse.json();
        answer.set("Something went wrong")
        console.log(err)
    }

    const result = await chatResponse.json()
    // console.log(result)
    if (result.data.message) {
        answer.set(result.data.message)
    } else {
        answer.set("I apologize, but I'm not programmed to understand certain types of language or slang. Could you please rephrase your statement using more common terminology?")
    }

    updateMessages(get(answer), 'assistant', 'idle');
    answer.set('')
};

const replace = (messages: ChatTranscript) => {
    store.set(messages);
};

const reset = () =>
    store.set({
        messages: [
            {role: 'assistant', content: 'Hello, I am your virtual assistant. How can I help you?'}
        ],
        chatState: 'idle'
    });

const updateMessages = (content: any, role: any, state: any) => {
    chatMessages.update((messages: ChatTranscript) => {
        return {messages: [...messages.messages, {role: role, content: content}], chatState: state};
    });
};

const handleError = <T>(err: T) => {
    updateMessages(err, 'system', 'error');
    console.error(err);
};

const streamMessage = (e: MessageEvent) => {
    try {
        if (e.data === '[DONE]') {
            updateMessages(get(answer), 'assistant', 'idle');
            return answer.set('');
        }

        if (get(answer) === '...') answer.set('');

        const completionResponse = JSON.parse(e.data);

        console.log(completionResponse)
        const [{delta}] = completionResponse.data;

        if (delta.content) {
            answer.update((_a) => _a + delta.content);
        }
    } catch (err) {
        handleError(err);
    }
};

export const chatMessages = {subscribe, set, update, reset, replace};
export const answer = writable<string>('');
