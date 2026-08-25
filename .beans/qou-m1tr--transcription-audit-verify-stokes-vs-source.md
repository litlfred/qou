---
# qou-m1tr
title: 'Transcription audit: verify the hand-typed GGM Stokes matrices / A-polynomial / 5_2 slopes against the source PDFs now that we have them all'
status: todo
type: task
priority: high
tags:
    - g3-aomega
    - integrity
created_at: 2026-08-11T10:50:00Z
updated_at: 2026-08-11T10:50:00Z
---

THE GAP (raised by the owner 2026-08-11: "do we have proof these are correct?"). Several
load-bearing Lean files take HAND-TRANSCRIBED literature data as defs. Lean proves everything
downstream but cannot verify the transcription — the sorry-free != derived boundary:

  FiveTwoDTSpectrumSplit.Splus0/Sminus0   "glyph-decoded" GGM eq (96)/(97)
  RouteANewtonPolygonDT.a41Monomials      A_{4_1} monomials (literature)
  RouteANewtonPolygonDT.fiveTwoMaxAbsSlope 5_2 boundary slopes {0,-4,-10} (RECALLED, weakest)
  qbeta_g3_ggm_stokes_41.py               GGM q-series (derived OCR-free — the strong one)

CURRENT MITIGATION (evidence, not proof): det S+ = det S- = 1; S+^T S- = 1 (exact inversion
between two SEPARATELY transcribed matrices — a typo would break it); the A-poly Newton
polygon is invariant under the reciprocal symmetry (M,L)->(M^-1,L^-1) [proved 2026-08-11 in
RouteANewtonPolygonDT.a41_monomials_reciprocal_symmetric]; the 4_1 tower matched through q^400.

NOW ACTIONABLE: every source PDF is in library/ (2012.00062v3, 2007.10190v2, 2111.04763v2,
2111.06645v3, 1208.1663v2, 1112.5179v1, 1604.02688v1, 1304.2705v1). Extract eqs (96)/(97)/(98)
with pymupdf and diff against the typed matrices; do the same for the A-polynomial. Note eq (17)
S+(x;q)^T S-(x^-1;q) = 1 was CONFIRMED in the source this session.
STILL NEEDS SnapPy (or a source) for the 5_2 boundary slopes — see qou-52sn.

## 2026-08-11 — STOKES MATRICES VERIFIED (stronger than a glyph-diff). Partial close.

Read GGM 2012.00062v3 eqs (96)/(97)/(98) from library/ (pymupdf). Result: the typed
5_2 Stokes matrices are NOT independent transcriptions at all — they are RECONSTRUCTIBLE
from the single eq-(98) DT-constant matrix

        [[ 0, 4, 3], [-4, 0, -3], [-3, 3, 0]]

via the elementary products GGM states:
   S+(0) = S_{s3s1} S_{s3s2} S_{s1s2}   -> [[1,4,0],[0,1,0],[-3,-9,1]]   == typed EXACTLY
   S-(0) = S_{s1s3} S_{s2s3} S_{s2s1}   -> [[1,0,3],[-4,1,-3],[0,0,1]]   == typed EXACTLY
and the independent structural identity eq (17) S+(0)^T S-(0) = 1 holds on the
reconstruction.

WHY THIS IS STRONG: the only input is a small unambiguous integer array {0,+-3,+-4}, and
the most typo-prone entry -9 is a PRODUCT ARTIFACT (-3*4 + 3), never a typed digit. A
transcription slip would have had to conspire with the product structure to survive.

Formalized sorry-free: QOU/QBeta/StokesMatrixProvenance.lean (splus_reconstructed,
sminus_reconstructed, minus_nine_is_derived, inversion_relation, dt_spectrum_three_four),
lean-direct exit 0.

RESIDUAL EXPOSURE (now minimized, not eliminated): that the eq-(98) array itself is read
correctly — one small matrix instead of the whole Stokes dataset. STILL OPEN in this bean:
the A_{4_1} monomials (mitigated by the proved reciprocal symmetry) and the 5_2 boundary
slopes (qou-52sn, the genuinely unverified input).
