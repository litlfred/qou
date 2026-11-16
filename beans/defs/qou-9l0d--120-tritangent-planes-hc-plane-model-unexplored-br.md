---
# qou-9l0d
title: 120 tritangent planes + HC plane model — unexplored Bring structures from Braden-DH 2024
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
    - 8f-flavour
created_at: 2026-08-04T17:32:49Z
updated_at: 2026-10-10T07:15:48Z
parent: qou-8lxd
---

Source: Braden & Disney-Hogg, "Bring's curve: old and new" (2024)

TWO unexplored structures from the Braden-DH paper:

1. 120 TRITANGENT PLANES:
   The canonical curve of genus 4 in P³ has 120 tritangent planes
   (planes tangent to the curve at 3 points). These are associated with
   the 120 ODD theta characteristics. Braden-DH decompose these under S₅
   as 120 = 60 + 60 (two orbits of size 60).
   
   120 = |S₅|. Each tritangent plane is in bijection with an element of
   the automorphism group. This is suggestive but may be coincidental.
   
   Physical question: do tritangent planes encode 3-body interactions?
   (3 tangent points per plane = baryon-like structure?) Speculative.

2. HULEK-CRAIG (HC) PLANE MODEL:
   Braden-DH give an explicit birational map from the P⁴ model
   (Bring's standard embedding) to a singular plane curve in P².
   The S₅ action becomes explicit collineations in PGL₃(C).
   
   This gives a COMPUTATIONAL handle on the S₅ action that QOU
   hasn't used. The explicit collineation generators could be compared
   with the S₃ colour sectors and the braiding generators.

3. UNIQUE S₅-INVARIANT SPIN STRUCTURE:
   Of 136 even theta characteristics, exactly 1 is S₅-invariant.
   This is the Szegő kernel divisor. The orbit decomposition is
   136 = 1 + 15 + 60 + 60.
   
   ANTI-FITTING: This is a theorem of algebraic geometry, NOT a QOU
   prediction. Do not claim "QOU derives a unique vacuum."

4. X₀(50) MODULAR QUOTIENT:
   Bring's Jacobian J(B) ∼ (50a)⁴. The level-50 modular curve
   appears. 50 = 2 × 5². Does this connect to any QOU modular data?
   Needs exploration.

## Progress Note (2026-11-16)
- Formalized Bring curve genus g=4 theta characteristics (256 = 136 even + 120 odd) and 120 tritangent planes S_5-orbit decomposition (36 even + 60 odd + 24 C_3 bitangents) in `QOU/Eightfold/BringThetaBruhatAndMesonH3.lean` (`bring_tritangent_120_and_theta_256_certificate`) + 50-dps probe `bring_theta_bruhat_and_meson_h3_probe.py` (PR `litlfred/qou#8163`, head `bc5c91877bf9516be8cbcc8cd12c1a6501a5e983`).
