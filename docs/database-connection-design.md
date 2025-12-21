# MongoDB Connection Design

- Database: MongoDB Atlas, database name `edupresence`.
- Connection string from Atlas stored in `.env` as `MONGODB_URI`.
- Backend module location: `backend/src/config/mongo.ts`.

## Pooling

- Use Node MongoDB driver (or Mongoose) with:
  - `maxPoolSize = 50`
  - `minPoolSize = 5`

## Retry strategy

- On startup, if connection fails:
  - Retry up to 5 times with exponential backoff (1s, 2s, 4s, 8s, 16s).
  - Log each failure with error message.

## Health check

- Express route `GET /health/db`:
  - Calls `db.command({ ping: 1 })`.
  - Returns `200` if ok; `503` if DB unreachable.

## Logging

- Log successful initial connection.
- Log slow queries and connection errors to a central logger.
