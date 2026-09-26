---
# qou-do3a
title: 'Fresh-look: uploaded-paper attack vectors on mass/binding gaps + q-diff order 2vs3 finding'
status: completed
type: task
priority: normal
created_at: 2026-07-19T00:00:34Z
updated_at: 2026-07-19T03:59:53Z
---


## Fresh-look assessment (2026-07-19) — uploaded papers vs mass/binding gaps

Papers (on main, commits 232049fd6e + 7b27b7865c): Masbaum twist-knot cyclotomic
(`masbaum2003`, WIRED 5₂ this session, #3993 merged); Garoufalidis–Lê "colored
Jones is q-holonomic" (`0309214v3`); Takata "colored Jones + A-polynomial for
twist knots" (`0401068v1`); Garoufalidis "characteristic & deformation varieties"
(`characteristic.pdf`); Laszlo–Pauly–Sorger "Hitchin connection monodromy"
(`MonodromyHitchinY.pdf`).

### KEY FINDING — q-difference ORDER is 2 for 4₁, 3 for 5₂ (the chiral jump)

Corpus-confirmed: the **4₁ colored Jones satisfies an ORDER-2 (2nd-order)
inhomogeneous q-difference equation** (`AJFigureEight.lean:92` "order-2
inhomogeneous q-difference operator"; `QCasoratianBarParity.lean` "order-2
qZeilberger operator"; Â-poly E-degree 2). The framework's **Q_β c_k kernel is
also 2nd-order** (= Hahn–Exton q-Bessel, `BindingQBesselKernel.lean`,
`q-bessel-second-order-qdifference`), and the **z(q) Taylor recursion is 3-term
= 2nd-order** (`QBetaPerBlockChiClosedForms.lean:1116`,
`qbeta-z-recursion-to-ck-recursion-bridge`).

Takata (+ Garoufalidis–Koutschan): the **5₂ colored Jones is ORDER-3**, 6₁ order-4
— the recursion order rises by one per twist. Since 5₂ is the chiral knot whose
bar-ASYMMETRIC Masbaum coefficients carry the Q_β odd datum (this session), the
**order jump 2→3 (4₁→5₂) is precisely where the bar-odd content lives**: the
bar-EVEN channel is captured by the 2nd-order (q-Bessel / 4₁-amphichiral) kernel;
the bar-ODD channel is the extra 3rd-order term the chiral twist adds. Sharp,
testable, and NOT a fit.

### Attack vectors — honestly, MOSTLY ALREADY-TRACKED gaps, now with paper inputs

The corpus-grep discipline shows the framework already identified these routes;
the papers supply authoritative *inputs*, they do not open virgin ground:

1. **Binding kernel R(q,x) depth ← twist/Borromean Â-polynomial (q-holonomic).**
   `binding-genfun-qdifference.lean` (L3) reduces binding to a depth-d q-difference
   kernel R whose existence is the *conjectural input*; **GAP-3 = bean `qou-6poy`**
   ("derived R(q,x) q-difference weight kernel"). Garoufalidis–Lê GUARANTEES the
   (Borromean) colored Jones is q-holonomic ⇒ R has FINITE definite depth; Takata
   gives the explicit twist-knot recursion → A-polynomial (order 3/4) as the
   template. STRONGEST mass/binding vector: it could fix R's depth from geometry,
   not fit it. Feeds `qou-6poy`, `n920` (Borromean AJ), `moqg` (Borromean tower),
   `c7vs` (EPIC AJ-operator unification), `z2bn` (Lever-1 fibre q-difference).

2. **Δ_λ mixed-sign ← cyclotomic-coefficient signs (evades the KL-positivity
   prune).** PROBE-4 was pruned because Δ_λ is mixed-sign but KL weights are
   non-negative; the Nakayama route was refuted because the natural pivotal twist
   is the CONTENT grading, while Δ_λ needs the ROW grading q^{2n(λ)} (−1 on
   odd-n(λ)) — see `deltalambda-grho-nakayama-morphism.witness.json`. The Masbaum
   cyclotomic coefficients C_{K,n} ARE mixed-sign (C_{5₂,1}<0, C_{5₂,2}>0) — a
   structural mixed-sign source KL/content-grading could not supply. CONCRETE
   TEST (not yet run): do the cyclotomic-coefficient signs realise the row-grading
   q^{2n(λ)} pattern? If yes, a genuine (non-fit) Δ_λ source. Feeds `b9ra`
   (Δ_λ-ansatz audit), the Nakayama refutation, Option-E ledger.

3. **q_0 / substrate ← A-polynomial distinguished point (Subgoal-2).** AJ says the
   q→1 limit of the recursion IS the A-polynomial = SL2(C) character variety = the
   geometric ρ_∞ face (the two-faces bridge, #3970). Takata/Garoufalidis give the
   twist-knot A-polynomial + the characteristic/deformation variety. Attack vector
   for deriving q_0 geometrically (Subgoal-2, open-for-all 2026-07-11) — but a
   curve, not a point; needs the extra arithmetic/quantum-modular condition to
   pin q_0. NOT a closure. Feeds the s5-so3 keystone geometric route.

4. **Hitchin connection monodromy ← the ħ↔2πi/N resummation wall.** The Hitchin
   connection monodromy = CS/WZW mapping-class-group rep = the framework's Hecke
   braiding; relates flat sections across Stokes sectors. SPECULATIVE for
   mass/binding; relevant to the two-faces resummation (Q_β). Bean `qou-oduj`.

### Discipline
Anti-laundering holds: these are DERIVATION ROUTES to pursue, not closures. Every
"attack vector" above is scope-(a) at best until a probe/derivation lands; #2's
KL-evasion is a real structural observation but the sign-map test is unrun; nothing
is wired to production. No fit; no c_k. The papers' value = authoritative inputs
(explicit twist recursion, q-holonomicity guarantee, A-polynomial) to gaps the
corpus already tracks (qou-6poy, n920, c7vs, z2bn, b9ra).
