---
# qou-z962
title: HS matrix-O pairing probe — feed the combiner ⟨O,(G−μ)⁻¹O⟩
status: scrapped
type: task
priority: high
created_at: 2026-07-25T02:16:56Z
updated_at: 2026-07-25T02:19:09Z
parent: uz9i
---

Primary live c₃ lead (sibling #4085 confirms UNTOUCHED). Feed the bar-odd combiner the MATRIX O=½(S⁺−S⁻) (GGM Stokes, 52.8% off-diagonal) via Hilbert–Schmidt pairing ⟨O,(G−μ)⁻¹O⟩_HS instead of the scalar φ_odd. Sees the off-diagonal the scalar trace discards. Recipe (Frobenius review): reuse qbeta_c3_barodd_knot_operator_gram_probe.py for the 5₂ Gram G; load O from qbeta-5two-stokes-barodd-index.witness.json; resolvent pole μ(q) MUST be a derived geometric eval-map value (Thurston gluing / Faddeev-Φ_q pole; bean qou-zol3 z(q₀) eval map), NOT tuned (else fit). Honest: smooth×smooth is smooth — won't close c₃ by itself; the swing lives in the geometric dressing. scope-(a).
