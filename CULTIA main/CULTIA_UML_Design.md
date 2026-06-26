# CULTIA - Complete UML Design Specifications

This document provides a graphical representation of the CULTIA platform using UML diagrams (Mermaid syntax). It covers the system's structure, behavior, and interactions.

---

## 1. Component Diagram (System Architecture)
The component diagram shows the high-level organization of the CULTIA system and the dependencies between its major parts.

```mermaid
componentDiagram
    component [Frontend Layer] as Frontend
    component [Backend API (Flask)] as Backend
    component [AI/Chatbot Engine] as AI
    component [Database (SQLite)] as DB
    component [External Services] as External
    component [Admin Panel] as Admin

    Frontend --> Backend : REST API (JSON)
    Backend --> DB : SQL Queries
    Backend --> AI : Knowledge Retrieval
    AI --> DB : JSON Data (Tribes/Legends)
    AI --> External : Gemini/Wikipedia APIs
    Admin --> Backend : Admin API Endpoints
    Admin --> DB : Management Queries
```

---

## 2. Use Case Diagram
This diagram illustrates the primary interactions between different actors (User, Admin) and the system.

```mermaid
useCaseDiagram
    actor "User" as User
    actor "Admin" as Admin

    package "CULTIA Platform" {
        usecase "Register/Login" as UC1
        usecase "Chat with Cultural AI" as UC2
        usecase "Read Folklore Stories" as UC3
        usecase "Complete Quiz" as UC4
        usecase "View Dashboard & Points" as UC5
        usecase "Learn Languages" as UC6
        usecase "Manage Users" as UC7
        usecase "Configure Gamification" as UC8
        usecase "Review Analytics" as UC9
    }

    User --> UC1
    User --> UC2
    User --> UC3
    User --> UC4
    User --> UC5
    User --> UC6

    Admin --> UC7
    Admin --> UC8
    Admin --> UC9
    Admin --|> User : Inherits Actions
```

---

## 3. Class Diagram (Backend & Data Models)
The class diagram represents the structure of the backend application, focusing on the data models and the relationships between them.

```mermaid
classDiagram
    class User {
        +int id
        +string first_name
        +string last_name
        +string email
        +string password
        +string role
        +datetime created_at
        +login()
        +register()
    }

    class Achievement {
        +int id
        +int user_id
        +string type
        +string name
        +int points
        +datetime earned_at
    }

    class FolkloreStory {
        +string story_id
        +string title
        +string tribe
        +int base_points
        +string content
    }

    class FolkloreProgress {
        +int user_id
        +string story_id
        +int current_progress
        +bool is_completed
        +datetime completed_at
    }

    class QuizResult {
        +int user_id
        +string quiz_id
        +int score
        +float percentage
        +datetime date_taken
    }

    class Chatbot {
        +process_query(query)
        +detect_intent(query)
        +get_response(tribe, intent)
    }

    User "1" -- "*" Achievement : earns
    User "1" -- "*" FolkloreProgress : tracks
    User "1" -- "*" QuizResult : achieves
    FolkloreStory "1" -- "*" FolkloreProgress : referenced_by
    Chatbot ..> User : assists
```

---

## 4. Sequence Diagram (Story Completion Flow)
This diagram details the step-by-step process of a user completing a folklore story and receiving rewards.

```mermaid
sequenceDiagram
    participant U as User (Frontend)
    participant B as Backend API (auth.py)
    participant DB as SQLite Database
    participant G as Gamification Service

    U->>B: POST /api/folklore/progress/{story_id}/complete
    B->>DB: Check if story already completed for user
    DB-->>B: Status (Already complete or Not)
    
    alt Not Completed
        B->>DB: Update folklore_progress (is_completed=1)
        B->>G: Calculate points for story
        G->>DB: Insert Point Transaction
        G->>DB: Update User Total Points
        B-->>U: JSON {success: true, points_awarded: 20}
        U->>U: Show Celebration Modal
    else Already Completed
        B-->>U: JSON {success: true, already_completed: true}
        U->>U: Show "Already Completed" UI
    end
```

---

## 5. State Diagram (Folklore Story Progress)
This diagram shows the various states a story can have for a particular user.

```mermaid
stateDiagram-v2
    [*] --> Locked: New Account
    Locked --> Available: Default State
    Available --> InProgress: User Starts Reading
    InProgress --> InProgress: User Reads More
    InProgress --> Completed: User Clicks "Complete Story"
    Completed --> [*]: Points Awarded
```

---

## 6. Activity Diagram (AI Chat Processing)
This diagram describes the logical flow of the AI chatbot when processing a user query.

```mermaid
flowchart TD
    A[Receive Query] --> B{In Scope?}
    B -- No --> C[Return Out-of-Scope Message]
    B -- Yes --> D[Extract Tribe & Intent]
    D --> E{Local Data Found?}
    E -- Yes --> F[Format Structured Response]
    E -- No --> G{LLM Available?}
    G -- Yes --> H[Call Gemini/Ollama Fallback]
    G -- No --> I[Call Wikipedia API]
    H --> J[Synthesize Response]
    I --> J
    F --> K[Return Final Response]
    J --> K
```
