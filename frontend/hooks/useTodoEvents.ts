import { useEffect, useCallback } from "react";

export function useTodoEvents(onEvent:(event:MessageEvent)=>void) {
    const stableOnEvent = useCallback(onEvent, []);
    
    useEffect(() => {
        const eventSource = new EventSource("http://localhost:8000/events");

        eventSource.onmessage = (event) => {
            console.log("Received event:", event.data);
            stableOnEvent(event);
        };

        eventSource.onerror = (error) => {
            console.error("EventSource error:", error);
            eventSource.close();
        }; 
        return () => {
            eventSource.close();
        }; 
    }, [stableOnEvent]);
}
