# The dominant summand's own log-weight carries no connected many-body term at A ≤ 4 — it is a bond functional plus a word-free weight

**Date.** 2026-09-12
**Bean.** `qou-m8f3` (the live remainder of `qou-brng` after PR #7181)
**Branch / PR.** `claude/dominant-summand-extensive-test-2026-09-12`, #7200
**Producer.** [`computations/brng_dominant_summand_ursell_probe.py`](../../computations/brng_dominant_summand_ursell_probe.py)
→ `brng-dominant-summand-ursell.witness.json`, **14/14 assertions**, 60 dps,
proton pin `Q_50_DIGIT_STR`, convention D `z = q³/(q²+1) = 0.6126880371…`.
**Lean.** [`QOU/Mass/OneRowBlockLetterProduct.lean`](../../content/quantum-observable-universe/lean/QOU/Mass/OneRowBlockLetterProduct.lean)
— generic ring, the product formula for a one-dimensional block's character.
**⚠ NOT compiled here** (see §7).
**Scope.** **(b)** at `A ≤ 4`, with the invariant named in §3; **(a)** at
`A ≥ 6` (§5). Nothing wired, nothing fitted, no route selected by residual.

---

## 0. The question, and why it was open

PR #7181 proved that the *multiplicity* channel of the partition sum
`tr_M(β_A) = Σ_{λ⊢3A} y_λ χ^λ(β_A)` is `O(√A)` and cannot be the extensive
binding term. Bean `qou-brng` then scoped the only remaining place inside the
trace sum: the **dominant summand's own log-weight**

$$L(A) \;=\; \log\bigl|\,y_{\lambda^*}\,\chi^{\lambda^*}(\beta_A)\bigr|,
\qquad \lambda^* = \operatorname{argmax}_\lambda |y_\lambda \chi^\lambda(\beta_A)|.$$

It was genuinely undecided: `QOU/Mass/MarkovBondRuleForcesPairwise.lean` forces
`b₃ = 0` for any binding read off **`tr_M`** by a product-to-sum map, because
the bond rule `tr(x(σ_g + d)) = (z+d)·tr x` is a statement about the whole
trace. It says nothing about one block's character `χ^λ`, and `argmax` is not
a linear functional of the trace. So the connected three-body cumulant of
`L(A)` could have been zero, positive (AME's sign) or negative.

## 1. What was computed

For every typed cluster `(Z,N)` with `Z+N ≤ 4` — p, n, pp, pn, nn, ppp, ppn,
pnn, nnn, ppnn — and ⁶Li as a growth check:

1. the **live** atom word `atom_braid_word_3A(Z, N)` (default
   `intra_order="borromean"`, the alternating-core ruling of 2026-09-05, bean
   `qou-hu1f`) and its free word (`include_inter=False`), on `n = 3A` strands;
2. all `χ^λ` via `chi_general_word.chi_all_lambda_any` (window transfer for the
   non-monotone live word) and `y_λ` via
   `wedderburn_jones_markov.y_lambda_at(n, Q_MP)`;
3. the dominant summand **as the trace defines it**, `argmax |y_λ χ^λ|`;
4. `L_atom`, `L_free` (each at its own argmax) and the binding-like difference
   `ΔL = L_free − L_atom`, the exact analogue of the production law
   `B_sym = E₀·ln(tr_free/tr_atom)` in `mass_binding_dashboard` with the trace
   replaced by its largest term. Scale: `E₀ = m_e/(q₀(q₀−1)) =
   4.18598136329447589694… MeV` from `mass_binding_dashboard._constants()` — the
   constant the dashboard multiplies `ln(tr_free/tr_atom)` by. **No new scale.**
   (The #7181 probe carries `E₀/(1−ℏ²)`, 0.99 % away; every sign and ratio
   below is scale-free.)

Then the typed Ursell (cluster-cumulant) inversion — `b₁` per nucleon type,
`b₂` per pair type, `b₃` per triple type, `b₄` for ppnn — of `ΔL`, of two
controls, and of the decomposition in §3; plus the corpus **uniform-`e₂`**
convention in which the AME targets of `qou-brng` are stated
(`e₂ := B(²H)` for every pair; `b₃^unif(A=3) = B(3) − 3e₂`, so AME2020 gives
`b₃(³H) = +1.8081`, `b₃(³He) = +1.0443` MeV; audits 2026-08-29 Milnor /
2026-08-30 Ursell).

**Cache provenance.** The four committed per-partition caches
`chi-{deuteron,tritium,helium-3,helium-4}-h{6,9,9,12}-at-q0-50dps.witness.json`
carry `computedAt 2026-09-06`, `q0Anchor: proton`, producer
`chi_at_q0_via_hoefsmit_mpfr.py` calling `atom_braid_word_3A(Z, N)` with the
post-ruling default. The live recompute reproduces every `χ^λ` and `y_λ` in
them to **3.4e-49** (assertion). They are not stale; this probe recomputes
anyway and never reads them for a number.

## 2. The measurement

### 2a. Which block dominates — and it is the ONE-ROW block

| cluster | n | p(n) | trace argmax `λ*` (atom) | runner-up / dominant | share of Σ\|a_λ\| | trace argmax (free) | binding-sum argmax `\|yχΔ\|` (atom) |
|---|---|---|---|---|---|---|---|
| p | 3 | 3 | **[3]** | 0.099 | 0.910 | [3] | [3] |
| n | 3 | 3 | **[3]** | 0.162 | 0.860 | [3] | [3] |
| pp | 6 | 11 | **[6]** | 0.101 | 0.837 | [6] | [6] |
| pn = ²H | 6 | 11 | **[6]** | 0.299 | 0.693 | [6] | [5,1] |
| nn | 6 | 11 | **[6]** | 0.384 | 0.682 | [6] | [5,1] |
| ppp | 9 | 30 | **[9]** | 0.316 | 0.643 | [8,1] | [6,3] |
| ppn = ³He | 9 | 30 | **[9]** | 0.361 | 0.522 | [9] | [6,3] |
| pnn = ³H | 9 | 30 | **[9]** | 0.502 | 0.467 | [9] | [6,3] |
| nnn | 9 | 30 | **[9]** | 0.595 | 0.444 | [9] | [6,3] |
| ppnn = ⁴He | 12 | 77 | **[12]** | 0.754 | 0.348 | [9,3] | [9,3] |
| ⁶Li | 18 | 385 | [15,3] | 0.718 | 0.240 | [13,5] | [12,6] |

Two facts to hold apart, because the corpus has been using the word "dominant"
for both:

* **The trace's dominant summand is the one-row block `[3A]` for every cluster
  with `A ≤ 4`**, with the runner-up at most 75.4 % of it (⁴He). At ⁶Li it is
  the two-row `[15,3]`.
* **The binding-sum argmax `|y χ Δ|` is `[5,1] / [6,3] / [6,3] / [9,3]`** for
  ²H / ³H / ³He / ⁴He — *exactly* the list in
  `QOU/BraidKnot/BindingConcentration.lean`'s header ("D: (5,1), T/³He: (6,3),
  ⁴He: (9,3)"). So that file's "dominant partition" is the argmax of the
  **binding sum**, not of the trace, and that list **survived the 2026-09-05
  word change** unchanged. §6 has the docstring consequence.

### 2b. The one-row character is a product over letters

Each letter of the atom word is `c·σ_g + d·1` (`(c, d, g)` triples). The
one-row block is one-dimensional, its character is a ring homomorphism with
`σ_g ↦ q`, so

$$\chi^{(n)}(\beta) \;=\; \prod_{\text{letters}} (c\,q + d).$$

Verified on every atom and free word: max error **1.2e-49** (assertion).
Formalised generically in `OneRowBlockLetterProduct.lean` (§7).

### 2c. The atom word is a CHAIN, and that decides the control

`atom_braid_word_3A` builds `p…p n…n` with **`A−1` interfaces**: `(Z−1)` pp,
one pn (if both present), `(N−1)` nn — a linear layout, not `C(A,2)` bonds
(#7155). A complete-graph Ursell inversion of any edge-additive quantity
therefore returns `b₃ = −b₂(missing edge)` etc. The invariant to test is
**chain-edge additivity**, `X(Z,N) = (Z−1)X_pp + X_pn + (N−1)X_nn`, and:

| quantity | chain-edge residual (max over A ≤ 4) | reading |
|---|---|---|
| full trace `log(tr_free/tr_atom)` | **5.3e-50** | the `tr_M` bond rule holds on the LIVE word; `b₂(pp) = ln(1/z_D) = 0.48989938425513485141` to all printed digits |
| dominant summand, same block (`ΔL` with `y` cancelled) | **7.4e-51** | letter product ⇒ exactly edge-additive |
| dominant summand `ΔL`, own argmax on each side | 0.944 | the whole non-additive part is the **free-side argmax switch** (§3) |
| binding-sum dominant `|yχΔ|` (secondary, §4) | 1.02 | two-row block; not letter-multiplicative; not expected to vanish |

(The first control, incidentally, is the first numerical confirmation of the
`qou-g8i1` bond rule on the post-ruling alternating word: the 2026-08-19
verification predates it.)

## 3. The decomposition, and where every non-additive piece lives

Write the atom's dominant log-weight as

$$L_{\text{atom}}(A) \;=\; \underbrace{\log y_{(3A)}}_{\text{word-free}}
\;+\; \underbrace{\textstyle\sum_{\text{letters}} \log|c\,q+d|}_{\text{chain-edge additive}}$$

and the binding-like difference as `ΔL = ΔL_sameblock + switch`, where
`ΔL_sameblock` is the free-vs-atom comparison **inside the atom's own block**
(`y_{λ*}` cancels) and `switch = log|a(free, argmax_free)| − log|a(free,
argmax_atom)| ≥ 0` is the amount by which the free word's own largest term
exceeds its one-row term — **a function of the free word only, which has no
bond in it**.

Typed cumulants (log units; MeV = `E₀ ×`):

| cumulant | `ΔL` (the test) | `ΔL_sameblock` | `switch` | `log y_(3A)` (word-free) | full trace (control) |
|---|---|---|---|---|---|
| b₂(pp) | −0.10434 | −0.10434 | 0 | −0.79521 | +0.48990 |
| b₂(pn) | −0.00551 | −0.00551 | 0 | −0.79521 | +0.67682 |
| b₂(nn) | +0.10434 | +0.10434 | 0 | −0.79521 | +0.90726 |
| b₃(ppp) | +0.14956 | +0.10434 | +0.04522 | +0.62166 | −0.48990 |
| b₃(ppn) | +0.00551 | +0.00551 | 0 | +0.62166 | −0.67682 |
| b₃(pnn) | +0.00551 | +0.00551 | 0 | +0.62166 | −0.67682 |
| b₃(nnn) | −0.10434 | −0.10434 | 0 | +0.62166 | −0.90726 |
| b₄(ppnn) | **+0.93851** | −0.00551 | **+0.94402** | −0.51584 | +0.67682 |

Read across:

* **`b₃(ppn) = b₃(pnn) = −b₂(pn)` exactly** (ratio `−1.000…` to the working
  precision, scale-free) — the chain's missing-edge accounting, not a connected
  term. AME's scale-free ratios are `b₃/e₂ = +0.813` (³H) and `+0.469` (³He).
* **`b₄(⁴He) = +0.9385` is 100.6 % `switch`** (the same-block part is
  `−0.0055`). In MeV, `E₀·ΔL(⁴He) = 3.93 MeV` is entirely the statement that the
  *free* word's largest term is `[9,3]` while the *atom's* is `[12]`. Nothing
  in it is an interaction.
* **`log y_(3A)` has alternating cumulants of order one** (`−0.795, +0.622,
  −0.516` ≈ `−3.33, +2.60, −2.16` MeV). They are identical for ³H and ³He,
  identical for ppp and nnn, and identical for any word on `3A` strands whose
  dominant block is one-row. A "connected `b₃ > 0`" read off `L(A)` alone would
  be this — a property of the Jones–Markov weight of the trivial block, with no
  nucleus in it.
* **The deuteron is anti-bound in this channel**: `e₂ = E₀·ΔL(pn) = −0.023
  MeV`. The pn interface letter has `c q + d = 1.0055 > 1`, so it *raises* the
  one-row character. The pp letter (`d = 0`) contributes `log q = +0.104`, the
  nn letter (`d = −h`) contributes `−0.104`; the sign pattern
  `b₂(pp) < b₂(pn) < b₂(nn)` is the colour-weighted interface's charge
  asymmetry, seen through one block.

### Uniform-`e₂` convention (MeV), the frame of the AME targets

| | AME2020 | trace's dominant summand | full trace |
|---|---|---|---|
| e₂ | 2.2246 | **−0.0230** | 2.8332 |
| b₃(³H) | +1.8081 | +0.4829 | −1.8685 |
| b₃(³He) | +1.0443 | **−0.3907** | −3.6156 |
| b₄(⁴He) | +9.2434 | +3.8825 | +2.6510 |
| b₃/e₂ (³H, ³He) | +0.813, +0.469 | −20.95, +16.95 | — |

The mirror pair comes out with **opposite signs** (³H positive, ³He negative);
both are the difference of two chain-edge terms (`(Z−1)L_pp + L_pn + (N−1)L_nn
− 3L_pn`), i.e. `L_nn − L_pn` for ³H and `L_pp − L_pn` for ³He, again with no
connected content.

## 4. Secondary: the BINDING-sum dominant summand (`argmax |y χ Δ|`)

Because `BindingConcentration.lean`'s "dominant partition" is this other
argmax, and because it is a **two-row** block whose character is *not*
letter-multiplicative, the same analysis was run on it, labelled secondary and
selected by no result:

| | AME2020 | binding-sum dominant (uniform-`e₂`, MeV) |
|---|---|---|
| e₂ | 2.2246 | 1.0052 (0.45×) |
| b₃(³H) | +1.8081 | **+1.0163** (0.56×) |
| b₃(³He) | +1.0443 | **+0.7470** (0.72×) |
| b₄(⁴He) | +9.2434 | **−4.2710** (wrong sign) |
| b₃/e₂ | +0.813, +0.469 | +1.011, +0.743 |

Typed: `b₃(ppp) = −4.92`, `b₃(ppn) = −1.26`, `b₃(pnn) = +2.34`, `b₃(nnn) =
+4.58` MeV — **monotone in `N−Z`** (steps ≈ 0.87, 0.86, 0.54 log-units), with
`b₃(ppn) < 0` for a bound nucleus and `b₃(nnn) > 0` for an unbound one; `b₄ =
−3.58` MeV typed.

**Reported, not wired, and this is the case the task anticipated:** a positive
`b₃` of the right sign for both mirror nuclei in the uniform frame, at the
wrong magnitude (0.56× / 0.72×), whose typed decomposition is dominated by a
charge-asymmetric term and whose `b₄` has the wrong sign. Wiring it would
re-open the `Δ_λ`-magnitude family through the back door
(`docs/audits/2026-08-02-deltalambda-value-proved-downstream-and-additive-term.md`).
Under §NO FITTING, its better AME numbers than §3 are not evidence for it —
they are the reason to say so here.

## 5. Growth with A, and where the (b) argument stops

| A | cluster | `E₀·ΔL` (trace's dominant) | `E₀·log(tr_f/tr_a)` (full) | AME B | AME / `E₀·ΔL` |
|---|---|---|---|---|---|
| 2 | ²H | −0.023 | 2.833 | 2.225 | −96.5 |
| 3 | ³H | +0.414 | 6.631 | 8.482 | 20.5 |
| 3 | ³He | −0.460 | 4.884 | 7.718 | −16.8 |
| 4 | ⁴He | +3.929 | 8.682 | 28.296 | 7.20 |
| 6 | ⁶Li | +8.508 | 14.530 | 31.994 | 3.76 |

At ⁶Li the dominant block is `[15,3]`, two-row, and §2b/§3 no longer apply.
`E₀·ΔL` grows there (8.5 MeV, 3.8× short of AME) — one point, no shape claim.
The `(b)` exclusion is stated for `A ≤ 4` only; for `A ≥ 6` the dominant
summand is a two-row block and its log-weight is an unmeasured **scope-(a)**
object beyond the single ⁶Li number above.

## 6. Implications

* **`qou-brng`'s live remainder is closed at `A ≤ 4`, negative.** The dominant
  summand's log-weight is `log y_(3A)` (word-free) plus a letter sum (chain-edge
  additive, exactly). It carries no connected many-body term with nuclear
  content. Invariant for the (b): one-row dominance (measured, margin ≥ 24.6 %)
  + ring-homomorphism letter-multiplicativity (exact; Lean §7). Classes B (a
  non-sign-definite bond energy) and D (fibre-level / full tower) of the
  2026-09-11 enumeration are untouched and stay live; nothing here reaches
  them.
* **`MultiplicityNotExtensive.lean`'s header** says "the dominant summand's
  own log-weight is untouched and is the live remainder". True on 2026-09-11;
  the follow-up should point here: *tested 2026-09-12, at `A ≤ 4` the dominant
  block is one-row and its log-weight is a bond functional plus `log y_(3A)`;
  the remainder moves to `A ≥ 6` (two-row dominant) and to classes B/D.*
* **`BindingConcentration.lean`'s docstring** conflates two argmaxes. Its list
  `(5,1)/(6,3)/(9,3)` is the **binding-sum** argmax `|yχΔ|` and is still
  correct under the live word; the **trace's** argmax it also invokes ("largest
  `|y·χ|`", item 1) is the one-row `[3A]` at every `A ≤ 4`, and the two
  disagree. Its item 3 ("`(n−k, k)` maximises `|y·χ|`") is therefore false as
  written for the trace and true for the binding sum. A one-line docstring
  correction; not made here (owner's file, ask-first rule).
* **`mass_binding_dashboard`'s chain law is confirmed on the live word** —
  `b₂(pp) = ln(1/z_D)` to 20 digits — by a control this probe did not set out
  to run.

## 7. The Lean, and its verification status

`QOU/Mass/OneRowBlockLetterProduct.lean`: over generic `[CommRing R]`, an
`R`-algebra `H`, and `χ : H →ₐ[R] R` with `χ(σ_g) = q`, the character of a
word of letters `c·σ_g + d·1` is `∏ (c q + d)` (`map_word_eq_prod`) and
factorises over concatenation (`map_word_append`). Two theorems, induction and
`simp`; no `sorry`, no `ℝ`.

**⚠ It was NOT compiled in this session.** The container had 7.8 GB free
against a ~9 GB Mathlib cache restore and the dispatch rule forbids the restore
below 8 GB; `lake build` is forbidden outright. The statement is
`map_list_prod`-grade and the probe verifies the identity it formalises to
1.2e-49, but a reviewer must run `lean -DautoImplicit=false -s 65536` (or the
library sweep) before treating it as verified. If it fails to elaborate the
fix is in the `simp` set (`AlgHom.commutes` + `Algebra.id.map_eq_self`), not in
the mathematics.

## 8. Options (judgement, not findings)

1. **Record and stop** (default; what this PR does). The (b) at `A ≤ 4` lands
   in `qou-brng`; `A ≥ 6` and classes B/D stay open. Cost: nil further. Risk:
   none; nothing moved.
2. **Extend to `A ≥ 6` on the two-row dominant** — the honest continuation of
   *this* channel. Needs sub-clusters up to `A = 6` (21 typed words, each
   seconds) and a statement of what a two-row character's non-multiplicativity
   can and cannot supply. Cost: one session. Risk: the secondary in §4 already
   shows a two-row block produces an `N−Z`-ordered `b₃`, so the likely outcome
   is another charge-asymmetry artefact; worth doing only with the typed
   decomposition in hand from the start.
3. **Follow the secondary's `b₃ > 0`.** Not recommended: it is a fit signature
   (right sign, wrong magnitude, wrong `b₄` sign, `N−Z` ordering), and pursuing
   it because its numbers are closer is precisely the ranking §NO FITTING
   forbids.

Recommendation: **1**, with **2** as the next front if the owner wants this
channel exhausted rather than left at the one-row boundary.
