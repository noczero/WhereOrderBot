import type {RequestHandler} from './$types';
import {json} from '@sveltejs/kit';

export const POST: RequestHandler = async ({request}) => {
    try {
        console.log("This is what")

        const requestData = await request.json();

        if (!requestData) {
            throw new Error('No request data');
        }
        console.log(requestData.messages)

        // get latest
        const userContent = requestData.messages[requestData.messages.length - 1].content

        const requestBody = {
            prompt: userContent
        };

        const chatResponse = await fetch('http://localhost:8081/api/v1/chat/completions', {
            headers: {
                'Content-Type': 'application/json'
            },
            method: 'POST',
            body: JSON.stringify(requestBody)
        });

        if (!chatResponse.ok) {
            const err = await chatResponse.json();
            throw new Error(err);
        }

        // console.log("HAIHIAHI")
        // console.log(await chatResponse.json())
        const result = await chatResponse.json()
        console.log(result)

        return new Response(result, {
            headers: {
                'Content-Type': 'text/event-stream'
            }
        });

    } catch (e) {
        console.error(e);
        return json({error: 'There was an error processing your request'}, {status: 500});
    }
}