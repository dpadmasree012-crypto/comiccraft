# Phase 6: Testing

- **Test Case 1:** Empty form submission → Result: Form validation prevents submission.
- **Test Case 2:** Valid prompt with all fields filled → Result: Multi-panel comic generated with matching images and story text.
- **Test Case 3:** Gemini API rate limit hit (HTTP 429) → Result: Graceful error page showing "Outline generation failed" with the rate-limit message.
- **Test Case 4:** Missing `static/` or `templates/` folder → Result: Startup crash — fixed by ensuring both directories exist.
- **Test Case 5:** Panel count mismatch between outline and story → Result: `split_story_by_panel()` falls back to even word-chunking.
- **Test Case 6:** PowerShell script execution blocked on Windows → Result: Resolved using `Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass`.