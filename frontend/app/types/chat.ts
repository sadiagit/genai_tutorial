export type Message = {
    role: 'user' | 'assistant' | 'system',
    content: string,
    sources?: string[]
}