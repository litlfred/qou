---
# qou-z9xt
title: 'A=4 Magnus EXACT: heavy partitions (dim 5632-7700) exceed container window'
status: todo
type: task
created_at: 2026-08-30T17:41:57Z
updated_at: 2026-08-30T17:41:57Z
---

mpfr A=4 run (#6273) stalls at 48/77: the 4 heaviest partitions (dim 5632,5775,5775,7700) take ~16min each at 3.8x and keep getting killed by container cycles before banking. Row-concentration says they contribute <0.1% so P(A=4)~-1.0576e11 (banked-48, matches mpmath). Options: (a) accept banked value + <0.1% residual bound as 'exact to achievable precision'; (b) intra-partition checkpointing; (c) dedicated long-window run. Sign already locked NEGATIVE (99.93%).
