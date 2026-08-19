---
# qou-hihk
title: '6th truncated-muon q0: clarabel_certify.rs:149 q_str=1.10998 feeds Stern-Brocot rationalisation (BLOCKED: no gfortran here)'
status: todo
type: task
created_at: 2026-08-19T21:19:18Z
updated_at: 2026-08-19T21:19:18Z
---

FOUND 2026-08-19 during the PR #5344 rebase, by grepping the truncated
spelling across ALL bins rather than the five the gram::Q_0 scope note named.

SITE. tools/hecke-engine/src/bin/clarabel_certify.rs:149

    let q_str = "1.10998";
    let q_max = 10_000_u64;
    let report = tighten_solution(&solver.solution, 3, q_str, q_max);

This is a SIXTH truncated-muon anchor, missed by both the qou-8q0u round-1
audit (which grepped only the full-precision spelling) and the corrected
gram::Q_0 scope note (which enumerated five bins). 1277 ppb off the proton
anchor.

WHY IT IS NOT FIXED IN #5344. The site takes a STRING, not an f64, because it
feeds a Stern-Brocot rationalisation of the SDP dual (q_max = 10_000). So the
replacement is not gram::Q_0 but the 50-dps decimal string
color_weight::convergence::Q0_50DPS
= "1.1099785827513808075916690956107688798744991218736".

That substitution is NOT safe to make blind: Stern-Brocot returns the best
rational approximation under a denominator cap, so changing the input digits
changes WHICH rational the dual is tightened to, and hence the certificate.
The gram::Q_0 scope note requires each site have "its output re-verified
rather than a blind substitution", and here that re-verification cannot be
run in this sandbox:

    cargo build --bin clarabel-certify --features clarabel-sdp
      -> netlib-src v0.8.0 build fails: "No CMAKE_Fortran_COMPILER could be
         found"; gfortran and f77 are both absent (make + cmake are present).

So the binary can be neither built nor run here, before or after. Changing it
would be exactly the blind substitution the discipline forbids.

TO CLOSE. On a host with gfortran: capture the certificate output before, swap
q_str to Q0_50DPS, capture after, and report which rationals moved and whether
any PSD block''s min_diag or max_denom_bits changed. If the tightened rationals
are unchanged at q_max = 10_000, say so -- that is the useful result either way.

ALSO NOTE. v9.rs:802 and v9.rs:888 already carry "WAS the 5-significant-digit
literal 1.10998" comments, i.e. a sibling fixed those two independently. The
truncated spelling has now bitten three separate audits; grep BOTH spellings.
