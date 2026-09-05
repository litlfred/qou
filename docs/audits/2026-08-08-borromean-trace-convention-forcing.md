# Borromean trace convention: forced or selected? (bean `qou-3qrv`)

## Headline — the corpus contradicts itself about which trace the mass channel uses

> The canonical proposition's own scope note says the mass and binding
> computations use the **full-Hecke Ocneanu** trace (convention **C**,
> `z = 1/(q^{1/2}+q^{-1/2})`). Production uses convention **D**. They differ by
> 195 ppm on β_Bor, and switching to the one the paper names moves m_p by
> **−197 ppm**, destroying the CODATA match.

Chapter and verse in **§4**. The same scope note additionally claims the two
traces "coincide … on writhe-0, π=id braids — which is why every *physical*
mass prediction is insensitive to the distinction"; β_Bor is such a braid, and
that claim is **false**, refuted by a probe already in this corpus.

This is the finding. It is not tidy and it should not be tidied: the clean
forcing argument in §3 is real, but it rests on a premise the corpus disputes
in the one place that speaks directly to the mass channel.

## Verdict — two parts, pointing opposite ways

1. **The bean's headline number is a false alarm.** The 6.7 % gap between
   convention D and `markov_peel.tr_M_atomic(1,0)` is **not** a trace-convention
   discrepancy. `tr_M_atomic(1,0)` traces a **different braid word**. There is
   no fifth convention and no 6.7 % convention ambiguity in the m_p formula.
   (§1)

2. **The real question — D vs C at 195 ppm — is half-open, and the open half is
   the load-bearing half.** The step "TL ⟹ D" is now **proved, sorry-free,
   uniquely**, with no experimental input (§3). The step "the mass fibre functor
   lands in TL" is **not established**, and is contradicted as above (§4).

So: reading **(a)** for the mathematics, reading **(b)** for the premise. D is
not numerology — it is a canonical object, uniquely characterised. But its
*selection over C* does not currently rest on an established categorical fact,
and D is the one that lands on CODATA. That is precisely the configuration the
bean was opened to test for, and it survives the test only if the premise is
independently settled (§5).

Nothing is wired, no tier changed, no production value altered.

---

## 1. The 6.7 % is a different braid, not a different trace

`tr_M_atomic(Z, N)` (`computations/markov/markov_peel.py:310`) traces the word
built by `atom_braid_word_3A` (`computations/mass_at_3A_proper.py:256`), which
for `(Z,N) = (1,0)` is **11 crossings**, not the 6-letter Borromean word. Per
`pyhecke/atom.py::nucleon_gen_chains` it decomposes as

| part | crossings | source |
|---|---|---|
| confinement core | `σ₀³` and `σ₁⁻³` (6) | `B₃ = (σ₀σ₁⁻¹)³`, but **grouped by generator** |
| quark pairs | `uu→σ₀`, `ud→avg₀`, `ud→avg₁` (3) | quark content `['u','u','d']` |
| gluon self-coupling | `σ₀²` (2) | ILP-derived |

Two independent reasons it is not `β_Bor`: five extra crossings, and the core is
`σ₀³σ₁⁻³` rather than the interleaved `(σ₀σ₁⁻¹)³` — a different braid closure.

**Decisive test** (`computations/probe3qrv.py`, proton pin q₀ = 1.1099785827513808,
50 dps). Tracing the **pure** `β_Bor` word through the *same*
`word_to_element → tr_M_element` machinery `tr_M_atomic` uses:

| object (same machinery, same q₀) | tr_M | ratio to D |
|---|---|---|
| `(σ₀σ₁⁻¹)³` — true β_Bor | **0.998562163836787266** | **1.000000000** (exact) |
| `σ₀³σ₁⁻³` — the grouped core alone | 0.180064539535501098 | 0.1803 |
| `atom_braid_word_3A(1,0)` — 11 letters | **1.145759692457300870** | 1.1474 (**14.74 %**) |
| convention D closed form | 0.998562163836787266 | — |

The pure Borromean word reproduces **convention D exactly**. The 14.7 % belongs
to the atomic word.

> **🛑 CORRECTED 2026-09-05 — every number in the table above changed, and one
> conclusion INVERTED. The qualitative finding survives; do not quote the old
> figures.**
>
> As first written this table read `0.998366622585715967` / `0.0685558643198896`
> / `1.06530614425444993`, and concluded *"The pure Borromean word reproduces
> **convention C** exactly — matching the registry's documented D−C gap of
> 1.9554e-4"*, with the atomic word at **6.68 %**.
>
> **That was correct when measured and is false now.** Re-running
> `computations/probe3qrv.py` **unchanged** reproduces the new column exactly,
> and the probe prints its own verdict: `|interleaved beta_Bor| / D =
> 1.0000000000000000000`. The pure Borromean word reproduces **D**, not C, and
> the 195.8 ppm C-gap this section attributed to it is gone.
>
> **Cause, attributed rather than guessed:** `c1a3299434` (2026-08-16,
> *"markov_peel: the docstring said convention C; the live path is D"*) migrated
> the `word_to_element` path this probe traces through. The audit predates that
> commit by eight days, so its numbers are pre-migration. `probe3qrv.py`'s own
> `z0 = q₀³/(q₀²+1)` was convention D all along — the C came in through
> `markov_peel`, which is exactly what `c1a3299434` fixed.
>
> **Cross-checked against an independent implementation** before correcting:
> the Frobenius pairing `Σ_λ y_λ χ^λ` (mpmath, 60 dps, Hoefsmit seminormal,
> `y_lambda_su_n(3, q, 2)`) agrees with `tr_M_element` at **ratio 1.0** on both
> words. Two implementations, one answer; the old table is the outlier.
>
> **What survives, unchanged and still the point of this section:** the grouped
> core is **not** β_Bor (0.1801 against 0.9986 — 82 % off), the atomic word is
> not β_Bor for the two independent reasons stated above, and comparing
> `tr_M_atomic` to `tr_M(β_Bor)` remains a **category error**. Only the
> magnitudes and the C-label moved. Re-measured under `qou-hu1f`; probe
> `computations/probes/nf_vs_canonical_word_order_probe.py`. The bean's phrasing *"convention D for the same braid at the same q₀"* is
the error; the braids differ.

**Consequence for the registry.** `tr_M_atomic` should not be listed as a
candidate Borromean trace convention. It answers a different question (the full
atomic braid of a nucleon, including quark-pair and gluon crossings), and
comparing it to `tr_M(β_Bor)` is a category error.

## 2. D and C are two members of the Ocneanu family — both legitimate

`computations/probe3qrv_ocneanu.py`, exact in `t = √q`:

- `sp.cancel(D − Σ_λ y^J_λ χ^λ) = 0` with `y^J = ([4]_q/[2]_q³, 1/[2]_q², 0)`.
  **D is exactly the H₃ Markov trace whose three-row weight vanishes.**
- `Σ_λ y_λ d_λ = 1` simplifies to `1` for **both** weight vectors. Both are
  properly normalised Markov traces.

| λ | `d_λ` | `y_λ` (D, Jones/TL) | `y_λ` (C, Wenzl z-trace) |
|---|---|---|---|
| (3) | 1 | 0.505404226503931 | 0.415395795360613 |
| (2,1) | 2 | 0.247297886748035 | 0.280929631031020 |
| (1³) | 1 | **0** | 0.022744942577347 |

This is not "one right trace and one bug". The production choice is a **choice
of Ocneanu parameter `z`**.

**A wrong test to avoid.** Dropping only `y_(1³)` from the *bridge* weights —
what the 2026-07-03 decision package's wording ("TL annihilates the 3-row
partition") most naturally suggests — gives **0.97562**, not D: off by 116× and
opposite in sign from `D−C`. The two surviving weights differ between the
conventions as well. `computations/probe3qrv_tl.py` records this failing test
so the next reader does not repeat it.

## 3. TL ⟹ D, uniquely — the forcing argument (new; sorry-free)

A normalised Markov trace on H₃(q) is determined by `(tr 1, tr σ₀, tr σ₀σ₁) =
(1, z, z²)`, so the weights are a 3×3 linear solve against the H₃ character
table (`computations/probe3qrv_zpin.py`):

```
y_(3)   = (q⁴z² + q³z + q²z² + 2qz + 1) / (q⁶ + 2q⁴ + 2q² + 1)
y_(2,1) = q(q²z − qz² + q − z) / (q⁴ + q² + 1)
y_(1³)  = q²(q⁴ − 2q³z + q²z² − qz + z²) / (q⁶ + 2q⁴ + 2q² + 1)
```

The Temperley–Lieb condition `y_(1³)(z) = 0` has **exactly two roots**:

| root | weight vector | status |
|---|---|---|
| `z = q` | `(1, 0, 0)` | **degenerate** — kills the 2-row block too; the trace collapses to the trivial character χ^(3), not faithful on TL₃ |
| `z = q³/(q²+1)` | `([4]_q/[2]_q³, 1/[2]_q², 0)` | **convention D**, exactly |

Note `z_D · [2]_q = q²`.

**Therefore: the unique Markov trace on H₃(q) that factors through TL₃ *and is
faithful on it* is convention D.** No residual freedom, no CODATA anywhere in
the chain.

Formalised in
[`QOU/BraidsAndKnots/MarkovTraceTLUniqueness.lean`](../../content/quantum-observable-universe/lean/QOU/BraidsAndKnots/MarkovTraceTLUniqueness.lean),
over a generic `[CommRing R] [IsDomain R]`, division-free (`q⁻¹` carried as `qi`
with `q·qi = 1`) — no `ℝ`, no ordering, no numerical q₀ (§7c fibre side):

- `markovWeights_eq_jones_of_threeRow_eq_zero` — the uniqueness theorem;
- `markovWeights_degenerate_root` — the `z = q` solution is real, so the
  faithfulness hypothesis is **load-bearing**: drop it and the conclusion is
  *false*, not merely unprovable;
- `threeRow_ne_zero_of_ocneanu_ne` — contrapositive: any faithful normalised
  Markov trace with `z·[2]_q ≠ q²` has `y_(1³) ≠ 0`, i.e. does not factor
  through TL. This separates C from D structurally.

`lean`-direct exit 0; zero sorries; `#print axioms` → `[propext,
Classical.choice, Quot.sound]` on all three.

The proof in one line: with `y_(1³)=0`, normalisation gives `y_(3) = 1−2y_(2,1)`;
the σ₀ equation collapses to `z = q − [2]_q·y_(2,1)`; substituting into the
σ₀σ₁ equation leaves `y_(2,1) = [2]_q²·y_(2,1)²`, and **cancelling the nonzero
`y_(2,1)` is exactly where the degenerate branch dies**, giving
`[2]_q²·y_(2,1) = 1`.

> This supersedes the derivation in
> [`h3-markov-wenzl-weights-proof.md`](../../content/quantum-observable-universe/mass-theory/h3-markov-wenzl-weights-proof.md)
> §Step 3, which obtains `y_(2,1) = 1/[2]_q²` **by comparing against the
> Borromean closed form**. That is fine for its own purpose but cannot serve as
> a forcing argument for the convention — it inputs the answer. The derivation
> above uses only the Markov axioms, the character table, and TL.

## 4. The premise is NOT established — and the corpus contradicts itself

Everything above is conditional on: **the mass fibre functor lands in
`Rep(SU_q(2)) ≃ TL`, not in the full H₃(q).** That premise is where the
epistemic weight now sits, and it is not currently carried.

**The contradiction.** `prop:h3-markov-wenzl-weights` is the canonical corpus
statement on these weights. Its context block
([`h3-markov-wenzl-weights-context.md`](../../content/quantum-observable-universe/mass-theory/h3-markov-wenzl-weights-context.md)
§Scope) says, verbatim:

> "The framework's **mass and binding computations** use a *different* trace:
> the **full-Hecke Ocneanu** Markov trace, with parameter
> z = 1/(q^{1/2}+q^{-1/2}) … Consequently the closed forms below should be read
> as the **Jones-polynomial** weights, **not** as the general tr_M y_λ used by
> the compute pipeline."

That is convention **C**. But production uses **D**:
`computations/canonical_mass.py:108` does
`from m_p_substrate_identity_50dps import F_Bor`, and `F_Bor`
(`m_p_substrate_identity_50dps.py:138`) is `trM_borromean(q)·[3]_q!/q³` where
`trM_borromean` (line 119) is the D closed form. The
[2026-07-03 decision package](2026-07-03-trace-convention-decision-package.md)
§1 consumer map records the same chain.

**So the paper says the mass channel uses C; the code uses D.** The 2026-07-03
audit's "principled reading" — that TL is documented a priori — cites the
closed-form proof block, but the *canonical proposition on these very weights*
asserts the contrary for the mass channel. The premise is not merely
unsupported; it is disputed inside the corpus.

**A second, checkable error in the same Scope note.** It claims the two traces
"coincide … on the observable combination carried by writhe-0, π=id braids —
which is why every *physical* mass prediction is insensitive to the
distinction." β_Bor **is** writhe-0 with π=id, and `D − C = 1.9554e-4` there
exactly (a nonzero rational function, not numerical noise). The 2026-07-03
production-impact probe measures the consequence: switching the mass pipeline
D→C moves m_p by **−197 ppm**, destroying the CODATA match. The mass prediction
is not insensitive to the distinction — it is maximally sensitive to it. Both
claims in that Scope note need correction; that is a follow-up, not done here.

## 5. What would close it

The remaining question is **not** "which trace value" — it is a single
categorical fact:

> Does the Archimedean/fibre functor for the **mass** channel land in
> `Rep(SU_q(2)) ≃ TL₃`, or in the full `H₃(q)`?

If TL: §3 forces D, the m_p derivation is clean, and the corpus needs the Scope
note corrected. If full H₃: production is on the wrong trace by 197 ppm and the
μ–p tension baseline is measured against the wrong object. There is no third
answer, and **the answer must not be read off which value matches CODATA** —
that is the failure mode this bean was opened to test for.

Concrete next steps (none taken here):

1. **Find or write the independent argument** that the mass channel's fibre is
   2-dimensional (spin-½ / `Rep(SU_q(2))`) rather than the full Hecke module.
   Candidate hooks already in-tree: `QOU/Knots/KauffmanTL3.lean`,
   `conj:s5-so3-fiber-action`.
2. **Reconcile the two corpus statements** — the closed-form proof block and
   `h3-markov-wenzl-weights-context.md` §Scope currently disagree about which
   trace feeds mass. One of them is wrong.
3. **Correct the "insensitive to the distinction" claim** (§4 above), which is
   refuted by an existing probe in the same corpus.
4. **Do not re-litigate the 6.7 %** — §1 settles it.

## Scope of the negatives here

Per AGENTS §"Before declaring refuted":

- §1 (the 6.7 % is a different braid) is a **positive structural identification**
  backed by direct computation of both objects, not a refutation.
- §3's exclusion of the `z = q` branch is a **scope-(b) structural exclusion**
  with a named invariant: `y_(2,1) = 0` at that root, so the trace is not
  faithful on TL₃ — Lean-proved in `markovWeights_degenerate_root`.
- §4 is **not** a claim that D is wrong or that m_p is fitted. It is the
  narrower, verifiable claim that the *stated justification* for D does not
  currently hold up, and that the corpus contains two mutually inconsistent
  statements about which trace the mass channel uses.

## Reproduce

```bash
cd computations
python3 -u probe3qrv.py          # 6.7% is a different braid word
python3 -u probe3qrv_ocneanu.py  # D == the y_(1^3)=0 Markov trace, exactly
python3 -u probe3qrv_zpin.py     # y_(1^3)(z)=0 has 2 roots; one is degenerate
python3 -u probe3qrv_tl.py       # the naive TL test that FAILS (0.97562)
```

Lean:

```bash
scripts/lean-verify.sh content/quantum-observable-universe/lean/QOU/BraidsAndKnots/MarkovTraceTLUniqueness.lean
```

---

## 6. Follow-up 2026-08-09 — C does not arise from ANY `Rep(SU_q(N))` fibre

§5 poses the remaining question as a disjunction:

> Does the Archimedean/fibre functor for the **mass** channel land in
> `Rep(SU_q(2)) ≃ TL₃`, or in the full `H₃(q)`?

This narrows the second branch. It does **not** close the question — it removes
one way of answering it.

**Argument.** A fibre functor into `Rep(SU_q(N))` induces the *quantum* trace,
whose Wedderburn weights are the quantum dimensions — the principal
specialisation `s_λ(1, q, …, q^{N-1})`, by hook-content

    s_λ  ∝  Π_{(i,j)∈λ}  [N + j − i]_q / [h(i,j)]_q ,   normalised Σ_λ y_λ f^λ = 1.

Implemented and self-tested in [`computations/y_lambda_su_n.py`](../../computations/y_lambda_su_n.py)
(33/33), **validated by reproducing convention D exactly at `N = 2`** — the
weight vector `(0.5054042, 0.2472979, 0)`, `y_{(1³)} = 0` on the nose, and the
implied `z = q³/(q²+1)`. So the machinery agrees with §3's independent linear
solve at the one point where both apply.

**Measurement.** Such a trace has `y_λ = 0` for every λ with more than `N` rows.
Convention C is **nonzero on the deepest partition `(1ⁿ)` at every `n` tested**:

```
  n     deepest λ with y_C ≠ 0      closest integer N     max |y_C − y_SU(N)|
  2          2 rows                       3                   0.0248722
  3          3 rows                       3                   0.0370251
  4          4 rows                       3                   0.0342957
  5          5 rows                       5→ none matches      0.0254170
```

so C forces `N ≥ n` for every `n`, i.e. no finite `N` — and the large-`N` limit
does not rescue it either, the deviation *growing* with `N`:

```
  n = 3:   N=3  0.0370251    N=4  0.0927924    N=5  0.1233687
           N=6  0.1422849    N=20 0.1901070
```

**Conclusion (scope-(b), named invariant: the row cap `y_λ = 0` for `ℓ(λ) > N`).**
Convention C is not the quantum trace of `Rep(SU_q(N))` for any `N`, finite or
in the limit. It is a genuine Ocneanu-family member lying outside the
quantum-group specialisations — consistent with the registry calling it
"pinned-by-definition" rather than forced.

**What this buys.** §5's disjunction sharpens from "TL, or full `H₃`" to:

> either the mass fibre lands in TL — and then §3 forces **D**, sorry-free —
> or it is **not a quantum-group fibre at all**.

In particular the escape route "perhaps C is the SU(3) flavour trace, so the
mass channel is already carrying the eightfold-way `N = 3`" is **closed**: C is
not SU(3) (max deviation 0.0370 at `n = 3`), nor SU(N) for any other `N`. That
route would otherwise be attractive, because the eightfold chapter needs `N = 3`
and C's effective non-integer index is `N = 2.5995` — nearer 3 than 2, and
therefore easy to over-read.

**Assumption, stated because the conclusion depends on it.** That a fibre
functor into `Rep(SU_q(N))` yields the quantum-dimension weights. Standard (it
is the quantum trace), but it is an input here, not something proved in this
corpus. If a fibre functor could induce a non-quantum trace, the exclusion
weakens to "C is not the *quantum* trace of any `Rep(SU_q(N))`".

**Not claimed:** that the fibre is TL; that D is correct; that C is wrong. The
owner decision in §5 stands untouched, and the rule that it must not be settled
by CODATA match applies unchanged — noting that under C the deuteron is provably
unreachable while under D it is reachable, which is exactly the kind of
match-flavoured evidence that rule exists to discount.
