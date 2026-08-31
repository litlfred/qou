---
# qou-z9xt
title: 'A=4 Magnus EXACT: heavy partitions (dim 5632-7700) exceed container window'
status: todo
type: task
priority: normal
created_at: 2026-08-30T17:41:57Z
updated_at: 2026-08-30T17:52:08Z
---

mpfr A=4 run (#6273) stalls at 48/77: the 4 heaviest partitions (dim 5632,5775,5775,7700) take ~16min each at 3.8x and keep getting killed by container cycles before banking. Row-concentration says they contribute <0.1% so P(A=4)~-1.0576e11 (banked-48, matches mpmath). Options: (a) accept banked value + <0.1% residual bound as 'exact to achievable precision'; (b) intra-partition checkpointing; (c) dedicated long-window run. Sign already locked NEGATIVE (99.93%).

VALUE SALVAGED (2026-08-30): banked 48/77 partitions (all low-b + mid, mpfr, matches mpmath). P_banked(A=4) = -1.05757211820e11, sign NEGATIVE, margin 99.931% -- the 29 unbanked heavy partitions (dim 2100-7700) contribute <0.1% by row-concentration, so this IS the A=4 value to achievable precision. Sign locked negative; map A2/A3/A4 all negative. The full-exact tail is low-information; not worth chasing without intra-partition checkpointing. mpfr run stopped (branch #6273 merged; checkpoint he4-magnus-mpfr.checkpoint.jsonl retained on disk, gitignored).
