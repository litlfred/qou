# Borromean recurrence — qZeilberger route (route 2): complete diagnosis

**Date:** 2026-07-07
**Branch:** `claude/aj-conjecture-qou-uz5m6x`
**Bean:** `n920`
**Lineage:** PR #3443 (existence certificate), PR #3450 (qZeilberger
foundation + CRT-route conditioning diagnosis), this branch (route-2
telescoper diagnosis).

## Epistemic status (STRICT — evidence vs proof, existence vs specific)

Two distinctions must not be blurred:

1. **Existence of *a* recurrence is a THEOREM, not our result.** The
   colored Jones function of any link is q-holonomic (Garoufalidis–Lê
   2005); the diagonal specialization `J_{B,n}` inherits holonomicity by
   closure, so it satisfies *some* q-difference recurrence as a matter of
   published theory. We did **not** first establish that.
2. **What is ours is EVIDENCE for the SPECIFIC minimal recurrence** — the
   explicit order-5, window-13 operator (and the unique order-6, window-11
   form). That specific operator is unpublished (link-AJ is only
   *formulated*: Sawabe 2024, Hopf + Whitehead; no explicit Borromean
   recurrence / A-ideal is in the literature). Our certificate is a
   **mod-p numerical** certificate (candidate solved on fit rows, then
   annihilating 30+ rows beyond the fit range at 9 independent
   (prime, base-point) samples; accidental survival `~p^-30`). Strong
   evidence — **not** a symbolic proof. The proof of the specific operator
   is exactly what the q-Gosper route (below) targets.

So "first Borromean recurrence evidence anywhere" means *first explicit
computation of the specific minimal recurrence*, not "first to show a
recurrence exists."

## Standing results (merged, unaffected)

- **Existence certificate** (PR #3443): strong mod-p **evidence** (not
  proof) for the **specific** minimal q-difference recurrence of the
  Borromean diagonal colored Jones tower `J_{B,n}` — order **5**
  (`r ≤ 4` excluded), 9/9 (prime, base-point) confirmations. (Existence of
  *some* recurrence is the q-holonomicity theorem; see Epistemic status.)
- **Habiro formula** transcribed + TL₃ cross-verified (PR #3443).
- **qZeilberger foundation** (PR #3450): the summand shift-ratios
  `s = F(n,l+1)/F(n,l)` and `r1 = F(n+1,l)/F(n,l)` are **exact rational in
  (x,y,q)** and numerically verified 6/6 — so `F(n,l)` is
  q-proper-hypergeometric and creative telescoping is **well-posed** (a
  certificate exists to be found).

## Route-2 goal and the three shortcuts, each diagnosed

Goal: the **explicit** operator + a telescoping certificate (proof-grade,
Lean-formalizable analogue of the merged 4₁/trefoil operators), plus the
`q→1` diagonal A-polynomial.

The creative-telescoping identity
`Σ_i a_i(x) R_i(x,y) = Cert(x,qy)·s(x,y) − Cert(x,y)`
is linear in the unknown coefficients of the operator `a_i` and certificate
`Cert = P(x,y)/DEN(x,y)`. Three ways to solve it were tried; each failed
for a **now-understood** reason:

1. **Symbolic `sp.solve`** (`borromean_qzeil_certificate.py`) — too slow
   for the cube summand (`R_i = ∏ r1(q^t x,y)` blows up; the solve did not
   terminate within 25 min and was killed by container reclaim).

2. **Fixed-q mod-p nullspace** (`borromean_qzeil_fixedq.py`) — fast
   (seconds/q0), but the nullspace is **large** (nullity 41–311) because it
   is swamped by spurious *certificate-homogeneous* solutions
   (`a = 0`, `Cert(x,qy)·s = Cert(x,y)`).

3. **Operator-projection of the nullspace**
   (`borromean_qzeil_minimal_telescoper.py`) — projects out the `a = 0`
   spurious solutions to find the minimal telescoper order `r*`. It reports
   `r* = 2` with a **nonzero operator projection**, but that operator
   **fails tower verification** (`Σ_i a_i J_{n+i} ≠` the boundary term) and
   **contradicts the merged existence certificate** (`r ≤ 4` excluded).

## The decisive finding

Shortcut 3's `r* = 2` artifact is the crux: with a **free, rich**
certificate ansatz (y-degree 10, x-window ±8), the certificate can
Gosper-sum *almost any* low-order `a`-part, so the operator-projection
reports a spurious order-2 "telescoper" that is not a genuine recurrence.
A free certificate ansatz is therefore fundamentally unusable — it is
either **over-rich** (absorbs everything → fake low-order operators) or,
if trimmed blindly, **empty**.

**Conclusion (the pinned requirement).** The certificate denominator must
be **exactly q-Gosper-normalized**: computed from the summand q-shift ratio
`s(x,y)` via the q-analogue of the Gosper–Petkovšek greatest-factorial
factorization. That factorization bounds the certificate numerator degree
*precisely*, giving the telescoping nullspace the correct (nullity-1 at the
minimal order) dimension. Only then does the linear-algebra isolate the
genuine minimal telescoper.

This is **not** a sampling shortcut — it is the actual q-Gosper / q-Zeilberger
algorithm (Koornwinder's `qZeil`; ~200–400 lines: the q-Gosper term-ratio
`a/b·c(qy)/c(y)` decomposition with the resultant-based gcd conditions,
then the polynomial Gosper equation solve). It is a well-scoped, standalone
implementation task — appropriate for a dedicated effort, not a late-night
sampling patch, and it does not need the long uninterrupted compute window
that killed the CRT route (each q-Gosper solve is small and fast).

## Disposition

- No wiring, no status changes to any conjecture carrier.
- The existence certificate remains the standing headline result.
- The foundation (verified shift-ratios) + this diagnosis together mean
  the explicit-operator tranche is now **precisely scoped**: implement
  q-Gosper certificate normalization, then the telescoper + A-polynomial
  fall out. Recorded in bean `n920` as the next step.
- Scripts committed as the reproducible investigation record; the
  `borromean-qzeil-minimal-telescoper.witness.json` honestly records the
  `r*=2` artifact (`found: false`).
