## Agentic AI Fundamentals

### 1. What is Agentic AI?

**Answer:**
Agentic AI is an AI system that can reason, plan, use tools, access memory, and perform actions autonomously to achieve goals.

---

### 2. How is an AI Agent different from a Chatbot?

**Answer:**
A chatbot mainly generates responses. An AI agent can plan, make decisions, use tools, maintain memory, and execute tasks.

---

### 3. What are the main components of an AI Agent?

**Answer:**
LLM, Memory, Planning, Reasoning, Tools, Execution Layer, and Monitoring.

---

### 4. What is the role of an LLM inside an Agent?

**Answer:**
The LLM acts as the brain, responsible for understanding requests, reasoning, planning, and deciding which tools to use.

---

### 5. What is Agent Planning?

**Answer:**
Planning breaks a goal into smaller executable tasks and determines the sequence of execution.

---

### 6. What is Agent Reasoning?

**Answer:**
Reasoning helps the agent evaluate information and determine the best next action.

---

### 7. What is Agent Memory?

**Answer:**
Memory stores user preferences, previous interactions, workflow state, and context.

---

### 8. What are Short Term and Long Term Memory?

**Answer:**
Short Term Memory stores current conversation context. Long Term Memory stores information across sessions.

---

### 9. What is Tool Calling?

**Answer:**
Tool calling allows agents to invoke APIs, databases, search engines, and external services.

---

### 10. How does an Agent decide which tool to use?

**Answer:**
The LLM analyzes the request, identifies the required action, and selects the most appropriate tool.

---

## ReAct, MCP & Multi Agent

### 11. What is the ReAct Framework?

**Answer:**
ReAct stands for Reason + Act. The agent reasons, performs actions, observes results, and repeats until completion.

---

### 12. Why is ReAct important?

**Answer:**
It improves accuracy by allowing agents to verify results and adapt their actions dynamically.

---

### 13. What is MCP (Model Context Protocol)?

**Answer:**
MCP is a standard protocol that allows AI models to communicate with tools, APIs, databases, and external systems.

---

### 14. Why is MCP becoming important?

**Answer:**
It simplifies tool integration and creates a standard interface between models and external resources.

---

### 15. What is a Multi Agent System?

**Answer:**
A Multi Agent System consists of specialized agents working together to complete complex tasks.

---

## RAG & Knowledge Retrieval

### 16. What is RAG?

**Answer:**
RAG combines document retrieval with LLM generation to produce accurate and context aware responses.

---

### 17. Why use RAG instead of Fine Tuning?

**Answer:**
RAG provides current information without retraining models, making updates faster and cheaper.

---

### 18. What are Embeddings?

**Answer:**
Embeddings are vector representations that capture the meaning of text and enable semantic search.

---

### 19. What is a Vector Database?

**Answer:**
A vector database stores embeddings and performs similarity searches for retrieval.

---

### 20. What is Chunking?

**Answer:**
Chunking splits large documents into smaller sections before generating embeddings.

---

### 21. Explain a complete RAG architecture.

**Answer:**

```text
Document
 ↓
Chunking
 ↓
Embeddings
 ↓
Vector Database
 ↓
Similarity Search
 ↓
Retrieved Context
 ↓
LLM
 ↓
Answer
```

---

## AWS Bedrock & AgentCore

### 22. What is Amazon Bedrock?

**Answer:**
Amazon Bedrock provides managed access to foundation models such as Claude, Llama, and Nova.

---

### 23. What is AWS AgentCore?

**Answer:**
AWS AgentCore is the runtime layer used to build, deploy, manage, and monitor AI agents.

---

### 24. What is the difference between Bedrock and AgentCore?

**Answer:**
Bedrock provides AI models. AgentCore provides planning, execution, orchestration, memory integration, and monitoring.

---

### 25. Why do we need AgentCore if Bedrock already exists?

**Answer:**
Bedrock provides intelligence. AgentCore provides the operational framework required to run agents.

---

## AWS Services Around Agents

### 26. Why is Lambda used in AI Agents?

**Answer:**
Lambda executes actions such as API calls, ticket creation, database operations, and workflow automation.

---

### 27. Why is DynamoDB used in AI Agents?

**Answer:**
DynamoDB stores memory, chat history, user preferences, and workflow state.

---

### 28. Why is OpenSearch used in AI Agents?

**Answer:**
OpenSearch stores embeddings and enables semantic search for RAG systems.

---

### 29. Why is CloudWatch important?

**Answer:**
CloudWatch provides monitoring, logging, observability, and troubleshooting for AI agents.

---

### 30. Explain a complete AWS Agent Architecture.

**Answer:**

```text
User
 ↓
API Gateway
 ↓
AgentCore
 ↓
Bedrock
 ↓
RAG Retrieval
 ↓
OpenSearch
 ↓
Lambda
 ↓
External APIs
 ↓
DynamoDB Memory
 ↓
CloudWatch Monitoring
 ↓
Response
```