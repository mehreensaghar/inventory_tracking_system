Stage 3: Scalable, Large Scale System

API Design Upgrades
- Switched to FastAPI for better async support
- real-time ops using background workers
- caching for faster inventory reads
- audit logging and scalable event handling

Scalability Strategy
- Ready for horizontal scaling
- Add message queue for real-time sync
- Read/write separation, rate limits, and load balancing in mind

Security
- Add API rate limits, OAuth2, and role-based access
