class ConversationMemory:
    def __init__(self):
        self.sessions = {}

    def _ensure_session(self, session_id: str):
        if session_id not in self.sessions:
            self.sessions[session_id] = {"messages": [], "context": {}}

    def add_message(self, session_id: str, role: str, content: str):
        self._ensure_session(session_id)
        self.sessions[session_id]["messages"].append({"role": role, "content": content})

    def get_messages(self, session_id: str) -> list[dict]:
        self._ensure_session(session_id)
        return self.sessions[session_id]["messages"].copy()

    def get_recent_messages(self, session_id: str, n: int = 10) -> list[dict]:
        self._ensure_session(session_id)
        return self.sessions[session_id]["messages"][-n:].copy()

    def set_context(self, session_id: str, key: str, value):
        self._ensure_session(session_id)
        self.sessions[session_id]["context"][key] = value

    def get_context(self, session_id: str, key: str, default=None):
        self._ensure_session(session_id)
        return self.sessions[session_id]["context"].get(key, default)

    def clear_session(self, session_id: str):
        if session_id in self.sessions:
            del self.sessions[session_id]
