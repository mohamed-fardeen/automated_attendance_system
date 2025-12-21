# Firebase / Cloud Storage Structure – EduPresence

Planned bucket: `automated-attendance-system` (or equivalent GCS/S3 bucket when enabled).

students/{studentId}/
  profilePhoto.jpg
  facialEmbedding.json
  documents/
    admissionProof.pdf

attendance/{classId}/{sessionDate}/
  attendanceReport.pdf
  videoFrames/
    frame_0001.jpg
    frame_0002.jpg
    ...
  logs/
    facialRecognitionLog.json
    ultrasonicLog.json

videos/{classId}/
  {sessionDate}_video.mp4
  {sessionDate}_thumbnail.jpg

reports/{collegeId}/
  dailyReport_{date}.pdf
  monthlyReport_{month}.xlsx
  complianceReport_{quarter}.pdf

## Naming conventions

- `studentId`, `classId`, `collegeId` are MongoDB ObjectIds.
- `sessionDate` format: `YYYY-MM-DD` (e.g., `2025-01-15`).
- Frame files: `frame_0001.jpg`, `frame_0002.jpg`, etc.

## Access control (high level)

- Students: read/write only under `students/{theirUserId}/`.
- Faculty: read attendance/videos for their `classId`.
- Admin: full access including `reports/{collegeId}/`.

## Notes

- Actual cloud storage (Firebase / GCS / S3) will be wired later after choosing a provider.
