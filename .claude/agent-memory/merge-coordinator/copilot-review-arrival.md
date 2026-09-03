# Does a Copilot review actually arrive? — and why nobody has measured it

Detail for the `MEMORY.md` BASELINE row. Bean `qou-gwe9` (reopened).

**Read this before quoting any figure about Copilot reviews in this repo**, and
before "correcting" the TRAP row in `MEMORY.md` in either direction. The
question matters because Copilot is the *only* live external gate — CI
auto-triggers are off repo-wide and Gemini is sunset — so whether a review is
coming decides whether waiting is a gate or a dead wait.

---

## The observations, and what each one is worth

| when | n | requested how | result | confounded by |
|---|---|---|---|---|
| 2026-08-23 | 5 | `request_copilot_review` on #5474, #5495, #5411, #5459, #5482 | **zero** on all five | force-pushes and re-requests |
| 2026-08-30 | 4 | qou#6122, fa#153, qou#6104, qou#6116 | **arrived**, ~3–4 min, substantive findings; two landed *after* a merge | not recorded whether pushes followed |
| 2026-08-31 | 2 | qou#6404, qou#6405 at 19:37 UTC | **zero** at 19:43 and 19:47 | #6405: I pushed twice after requesting. #6404: **clean** |

**So the clean sample size across the whole question is 1.** The 2026-08-31 pair
is not n=2 — #6405's zero is uninformative, because if a request binds to the
head SHA it was made against, my two later pushes could have superseded it.
#6404 is the clean one: a single commit, `c031248eb9`, untouched from 19:24,
requested at 19:38, `get_reviews` empty at 19:47.

## The confound nobody has controlled

Every one of the eleven observations above allows a push between the request and
the read, and **none of them records whether one happened**. That is the whole
difficulty: the two datasets that look like a contradiction (five zeros vs four
arrivals) are equally consistent with

- arrival being genuinely intermittent or rationed; **or**
- arrival being reliable, and every zero being a request invalidated by a
  later push.

Nothing measured so far distinguishes these. Treat "does it arrive" as
**unmeasured**, not as answered in either direction.

## The experiment that would settle it

1. Open a PR with a real payload (not an empty or throwaway one).
2. Call `request_copilot_review` **exactly once**.
3. **Make no further push to that branch** — no fixes, no doc tweak, no
   amend, nothing. This is the whole experiment; a single push voids the run.
4. Read `mcp__github__pull_request_read` with `method: "get_reviews"` at
   **5, 15 and 60 minutes**, and record the wall-clock of each read.
5. Record the outcome on `qou-gwe9` **with** whether any push occurred, so the
   next reader can tell a clean run from a confounded one.

A negative result here is as valuable as a positive one and must be recorded the
same way.

## Two things that are settled, and should not be re-measured

- **`get_check_runs` returning `total_count: 0` does not discriminate.** It
  returns 0 whether or not a review is coming, so it is not evidence of absence
  and must never be read as "none enqueued". Confirmed on both the arrival and
  zero cases.
- **The quota is real, and it announces itself.** Five requests across two repos
  in ~30 min on 2026-08-30 returned *"reached their quota limit"* explicitly. So
  a silent request that simply produces no review is **not** a quota refusal —
  on 2026-08-31 neither of my two calls errored, and both produced nothing.
  Do not re-request after every push; that is how the quota gets spent.

## Why the TRAP row must not be flipped on a single run

`MEMORY.md`'s Copilot row was already wrong once in the other direction — it
asserted reviews never arrive, on the n=5 zeros, and two PRs were merged on that
advice minutes before reviews landed carrying six findings including a real
correctness regression. Correcting it *back* on one clean zero would repeat the
same error with the sign flipped.

The stable wording, which survives both datasets, is what the row says now:
**rationed, arrival intermittent, `get_check_runs` does not discriminate, so
never read silence as "none coming" — but never block on it either.** Change it
only when the non-pushing experiment above has been run, and say how many clean
runs it rests on.
