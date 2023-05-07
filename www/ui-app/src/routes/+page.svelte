<script>

    import ChatInput from "../components/ChatInput.svelte";
    import ChatMessage from "../components/ChatMessage.svelte";
    import {chatMessages, answer} from '../stores/chat-messages';

    let query = '';

    const handleSubmit = async () => {
        answer.set('...');
        await chatMessages.set(query);
        query = '';
    };

</script>

<svelte:head>
	<title>Home / WhereOrderBot</title>
</svelte:head>

<section class="text-center">
<!--    <h1>WhereOrderBot - An AI-powered Chatbot</h1>-->
<!--    <small>by noczero</small>-->
    <h3 class="text-3xl font-medium leading-tight">
        WhereOrderBot
        <small class="text-neutral-500 dark:text-neutral-400"
        >An AI-powered Chatbot</small
        >
    </h3>
    <small>by noczero</small>
</section>

<section class="flex max-w-6xl w-full pt-4 justify-center">


    <div class="flex flex-col w-full px-8 items-center gap-2">
        <div class="h-[700px] w-full bg-black bg-opacity-20 rounded-md p-4 overflow-y-auto flex flex-col gap-4">
            <div class="flex flex-col gap-2">
                {#each $chatMessages.messages as message}
                    <ChatMessage type={message.role} message={message.content}/>
                {/each}

                {#if $answer}
                    <ChatMessage type="assistant" message={$answer}/>
                {/if}

            </div>
        </div>
        <form
                class="flex w-full rounded-md gap-4 bg-black bg-opacity-20 p-2"
                on:submit|preventDefault={handleSubmit}
        >
            <ChatInput type="text" bind:value={query} class="w-full"/>
            <button
                    type="submit"
                    class="bg-black bg-opacity-40 hover:bg-white/5 px-8 py-1.5 border border-black/40 ml-[-0.5rem] rounded-md text-white-300"
            >
                Send
            </button>
        </form>
    </div>
</section>

