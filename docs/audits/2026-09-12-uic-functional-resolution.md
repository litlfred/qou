# The unified-iterative-correction functional: resolving the block-vs-producer mismatch

**Date.** 2026-09-12
**Branch.** `claude/uic-functional-resolution-2026-09-12` · **PR** #7237
**Beans.** `qou-zlra` (found the mismatch, PR #7230), `qou-uicf` (this resolution),
`qou-sv7h` and `qou-brng` — both **stay open**.
**Lean.** `QOU.MassTheory.UICFunctionalSelection`, `QOU.MassTheory.UICLogSummandEven`
— ten declarations, all sorry-free, `lean`-direct exit 0.
**Probe.** `computations/probes/uic_functional_resolution_probe.py` — 16/16.

---

## 0. The owner's ruling, verbatim

> **"resolve functionals ... what lean provable"**
> — repo owner, 2026-09-12

This is an authorisation to resolve a mismatch that PR #7230 deliberately left
open, and it supplies the criterion: **the functional the corpus keeps is the one
that is Lean-provable** — a well-defined mathematical object admitting sorry-free
statements about itself. Not the one with better numbers, not the one written
first, not the one that is cheaper to compute.

It is recorded here verbatim because it is the reason a content block is being
changed at all. Under §"ASK THE OWNER BEFORE CHANGING THINGS" the default is to
ask; this ruling supplies the authorisation, and every individual change below
*additionally* satisfies exemption 2 (derived from the corpus) by pointing at the
artifact that decides it.

---

## 1. What the two sides actually say

Read at the primary sources, not at PR #7230's report.

### The content block

[`unified-iterative-correction.md`](../../content/quantum-observable-universe/mass-theory/unified-iterative-correction.md),
as it stood on `origin/main` at `173da443b66`:

| line | text |
|---|---|
| 1 | *"The per-partition binding corresponds directly to its **Frobenius positivity LP shadow price** $u_\lambda$, scaled by its $q$-hook product"* |
| 4-8 | $B_\lambda(Z,N) = m_e \cdot H_q(\lambda) \cdot u_\lambda \cdot (\ln\lvert \mathrm{tr}\,\mathbf{M}_\lambda^{(0..A)}\rvert - \ln d_\lambda)$ |
| 10 | *"Only multi-dimensional mixing partitions carry non-zero shadow prices. The total unified correction sums these **strictly over all** $\lambda$."* |

### The producer

[`computations/hecke_core_legacy.py`](../../computations/hecke_core_legacy.py):

| line | what it does |
|---|---|
| `:534`, `:543-548` | `_y = lp_shadow_price(λ)`; `_mu = q_laplacian_eigenvalue(λ)`; `_resolvent = 1/(_mu + S_REEB_PLANCK)`; `_resolvent_scale = _Hq * _y * _resolvent * M_E_MEV` |
| `:520` | `S_REEB_PLANCK = (q0 - 1.0) / q0` — the Planck-step Reeb frequency $s_\ast$ |
| `:1915` | `scale = e['C_lambda_resolvent_MeV']` — the accumulator reads the **resolvent-damped** scale |
| `:2078` | `raw_delta = s['scale'] * (log_cur - s['log_prev'])` |
| `:2089` | `s['final_tr_sign'] = 1 if tr_run > 0 else -1` |
| `:2183-2188` | Pass 2: `if s.get('final_tr_sign', 1) <= 0: gated_total += s['cumul_partition']` |
| `:2199`, `:2207` | returns `float(gated_total)` — **the gated sum is the return value** |
| `:1724-1726` | the producer's own docstring: *"NAMING CORRECTED 2026-09-05 (owner ruling; PR #6752). This read 'via LP-dual shadow prices'. The weights y_λ are **not** LP duals"* |
| `:328-360` | `lp_shadow_price`: *"NAMED for the LP shadow price; **it is not one** … This function solves no program. It evaluates a closed form."* |

So the producer computes

$$B = \sum_{\lambda\ :\ \mathrm{tr}\,\mathbf{M}_\lambda \le 0} m_e\, H_q(\lambda)\, y_\lambda\, \varrho_\lambda(s_\ast)\,\bigl(\ln\lvert\mathrm{tr}\,\mathbf{M}_\lambda\rvert - \ln d_\lambda\bigr).$$

### Prior corpus work (six-path grep, and it was not empty)

The grep was **not** a formality — half the resolution was already on `main`:

- **`prop:mass-coefficient-shadow-price`** ([`.md:30-36`](../../content/quantum-observable-universe/mass-theory/mass-coefficient-shadow-price.md))
  was **already corrected**, 2026-08-25 (`6b7d2ec4a8`) and 2026-09-05 (owner
  ruling, PR #6752): *"The function named for this proposition,
  `hecke_core_legacy.lp_shadow_price`, evaluates $y_\lambda = w_\lambda/d_\lambda -
  1/[k]_q!$ in closed form and **solves no program**."* The UIC block was simply
  left behind.
- **`QOU.ParticleInteractions.y_0_eq_zero_of_radical`**
  ([`operator_selection_lp.lean:390`](../../content/quantum-observable-universe/lean/QOU/ParticleInteractions/operator_selection_lp.lean))
  — sorry-free, over any commutative ring without zero divisors: the
  operator-selection LP's net-constraint dual is identically zero.
- **Bean `qou-8na1`** (`completed`): the same fact in ℚ(q), 18/18 checks, plus the
  sharper consequence — the committed f64 solve gives `y_star = e₀`, so *every*
  Frobenius shadow price except the identity index is exactly zero.
- **`computations/probes/uic_gate_justification_disproved_probe.py`** already
  concluded: *"complementary slackness cannot single out a partition set for a
  program whose optimum is identically 0 and whose minimiser set is a
  positive-dimensional face"* — and explicitly declined to name a replacement.
- **`computations/probes/uic_sign_forced_by_gate_probe.py`**: `B < 0` is forced by
  the gate for any nucleus.
- **`def:q-resolvent`** exists
  ([`q-resolvent.md`](../../content/quantum-observable-universe/quantum-observable-universes/q-resolvent.md)):
  $R_q(s) = (s + \widehat{\Delta_q})^{-1}$, whose $\lambda$-block scalar is
  $1/(\mu_\lambda + s)$ — so the producer's factor has a corpus definition to cite.

---

## 2. Applying the criterion: what each reading admits in Lean

### 2.1 The discriminator, and it is decisive

The block's summand reads the trace **only through $\lvert\mathrm{tr}\rvert$**, so
it is **even** in the trace. The producer's gate reads $\mathrm{sign}(\mathrm{tr})$
— which evenness has destroyed.

- `uicAll_sign_blind` (generic `[CommRing R]`) — flipping the sign of any subset of
  block traces leaves the block's stated total unchanged.
- `logRatio_even` (ℝ) — the displayed summand $\ln\lvert\tau\rvert - \ln d$ really
  is even, unconditionally, with no positivity hypothesis.
- `gate_not_a_function_of_displayed_data` — two trace vectors agreeing on **every
  value the displayed formula reads** whose gated totals differ.

**Therefore the block's formula, as written, cannot denote the producer's
functional.** This is not an editorial gap; it is a well-definedness failure
relative to the block's own variables, which is exactly the first discriminator
the criterion names. Something had to move regardless of the physics.

Measured, not merely proved — flipping every final trace's sign:

| atom | ungated | gated before | gated after |
|---|---|---|---|
| ²H | `-0.412212192245026906` (**identical**) | `-0.0895596830589506807` | `-0.3226525091860762` |
| ⁴He | `-0.274239771617400126` (**identical**) | `-0.0805867484776914329` | `-0.1936530231397087` |

### 2.2 The three divergences, scored

| # | claim | what the criterion finds | verdict |
|---|---|---|---|
| 1 | $u_\lambda$ is *"its Frobenius positivity LP shadow price"* | **Refuted, twice.** The net-constraint dual is provably 0 (`y_0_eq_zero_of_radical`, sorry-free) and the Frobenius duals of that LP are `e₀` (`qou-8na1`), so nothing is indexed by $\lambda$ at all. The one surviving reading the corrected upstream block allows — the *partition-indexed* solve, $y^\ast = (1,1,0)$ at $H_3$ — is also not it: the producer's closed form measures $(0,\ 0.166953658774,\ 0)$. Making this "provable" would require **assuming it as a class field**, which §"Axiomatization is NOT a Proof" counts *against* a reading. | **block moves** |
| 2 | the weight is $m_e H_q(\lambda) u_\lambda$, with no resolvent | $\varrho_\lambda(s) = 1/(\mu_\lambda + s)$ is a plain closed-form scalar with a corpus definition (`def:q-resolvent`), provably sign-free (`resolventScale_nonneg`), and the producer applies it. The block's formula is the producer's with one non-negative factor **deleted**. | **block moves** |
| 3 | *"sums these strictly over all $\lambda$"* | Both a gated and an ungated sum are Lean-*statable*. What the criterion settles is narrower and sharper: (i) the block's text is **factually false** about what runs; (ii) §2.1 shows the block's formula cannot even express the gate; (iii) the gate's *stated justification* is **disproved** — see §2.3. What it does **not** settle is which functional the physics should keep. | **block moves; producer does NOT** |

### 2.3 Complementary slackness justifies nothing that varies with the nucleus

The gate's own comment (`:2079-2084`, `:2176-2182`) derives it from complementary
slackness. For a constraint $\langle\Phi,\pi_\lambda\rangle \ge 0$, *tight* means
$\mathrm{tr} = 0$ — not $\mathrm{tr} \le 0$, which is what the code admits.

`uicGated_cs_eq` (sorry-free, generic): under the **genuine** condition every
selected block contributes the same value $f(0)$, so the total is
$\bigl(\sum_{\text{selected}} c_\lambda\bigr)\cdot f(0)$ — it reads **nothing**
about the atom and cannot distinguish two nuclei. A selection rule that cannot
vary with the nucleus cannot be the source of a nucleus-dependent binding energy.
`cs_selection_excludes_log_domain` adds that the CS set meets the domain of
$\ln\lvert\cdot\rvert$ nowhere.

Measured: **0 of 10** active blocks sit at $\mathrm{tr} = 0$ at the final state,
for both atoms. So the CS-justified gate is the empty sum.

Combined with `y_0_eq_zero_of_radical` — the LP prices nothing in the first place
— the gate has **no derivation at all**. It is a bare assertion.

### 2.4 The one thing PR #7230 ranked wrong

#7230's table calls divergence 2 *"a per-partition factor spanning ~100×"* and
divergence 3 *"the serious one"*. Measured on the totals rather than on the
factor's range, that ordering is backwards:

| atom | ungated / gated (the **gate**) | resolvent deleted / kept (the **omission**) |
|---|---|---|
| ²H | **4.6026535** | **4.1208754** |
| ⁴He | **3.4030381** | **9.8660639** |

At ⁴He the omitted resolvent is ~2.9× the gate's own effect. Both are factors, not
roundings; neither is the lesser finding.

(Also worth recording, because it makes the gate concrete: at ²H the gated set is
**four** blocks of ten of which exactly **one**, $(2,1,1)$, carries a non-zero
scale — the whole binding number is a single partition. At ⁴He it is $(3,1)$ and
$(2,2)$.)

---

## 3. Verdict, and its scope

**Resolved.** Divergences 1 and 2 are settled **against the content block**, each
on a corpus artifact a reviewer can open — a sorry-free Lean theorem and an
already-corrected upstream block for (1), a corpus definition and the producer's
own declared convention for (2). Both are exemption-2 changes under
§"ASK THE OWNER BEFORE CHANGING THINGS" independently of the ruling.

**Divergence 3 is resolved as a statement of fact, not as a choice of physics.**
The block now says what the producer computes and marks the gate as *asserted, not
derived*, citing the disproof. **The producer does not move.**

**Why the producer does not move, stated plainly.** The criterion establishes that
the gate is underived and that its stated justification is false. It does **not**
establish that the gate is *wrong* — a selection rule can be correct for a reason
other than the one given, which is exactly the scope-(a) / scope-(b) distinction
in §"Before declaring refuted". Dropping the gate would move every binding number
in the corpus by 3.4–4.6× on an argument that only refutes a justification. That
is neither a precision fix nor corpus-derived, so it asks. It is **not** asked
here, because the honest statement — "the gate is what runs, and it is asserted" —
is available without taking the decision.

**And the numbers do not break the tie either, which is the point.** Both readings
are wrong-signed against AME (²H: AME `+2.2246` MeV against `-0.0896` gated and
`-0.4122` ungated). Ranking them by residual would be the fit signature
§"NO FITTING" names; there is nothing to rank.

### What the criterion did NOT settle

Whether the gate belongs in the physics. That question needs the primal LP the
gate's comment invokes, which is not in `hecke_core_legacy.py`, and it is the same
decision `6b7d2ec4a8` declined to make one level up. It stays with `qou-sv7h`
(the sign / A-independence arc) and `qou-brng` (the extensive-term frontier), both
**open**.

---

## 4. Which side moved, and what it cost

**The content block moved; nothing else.** Diff:

- `unified-iterative-correction.md` — statement restated with $\varrho_\lambda$
  present, $u_\lambda$ defined in closed form rather than named as a dual, the
  summation range stated as the gated set, plus a new **Scope of the selection
  rule** section carrying the three facts of §2.3 and the epistemic mark.
- `unified-iterative-correction.ts` — `uses[]` gains `def:q-resolvent` (now
  hyperlinked from the prose; `prop:operator-selection-lp` is deliberately **not**
  added, being transitively reachable through `prop:mass-coefficient-shadow-price`
  and so a violation of *immediate neighbours only*). `authorNotes` carries the
  dated ruling per §4d.

**Blast radius: no number moves.** No producer was edited, no witness regenerated,
no dashboard re-scored. `beats_100x_scoreable` / `scoreable_total` unchanged; L1
and L2 unchanged. The two new Lean files are library-only with no content-block
`lean.ref` pointing at them, so no sidecar is invalidated by them.

**A latent render defect fixed in passing.** The pre-existing display block had a
line beginning `- \ln d_\lambda`, which the markdown list parser can hijack inside
`$$…$$`. Caught by the render-QA grep battery on this edit; reflowed so the
binary minus ends the previous line.

**A precision finding reported and NOT acted on.** `q_laplacian_eigenvalue`
accumulates `casimir_sum = 0.0` in float64 (`:292`) and `S_REEB_PLANCK` is a
float64 expression (`:520`), so every `C_lambda_resolvent_MeV` carries a
float64-limited resolvent. Against an mpf recomputation at `mp.dps = 70` the worst
relative gap over the ten active blocks is **2.54432e-16**, at $\lambda = (2)$.
**That figure is the floor of float64 arithmetic**, so it bounds the damage at
~1e-16 and cannot distinguish "correctly rounded" from "slightly wrong" — it is
not evidence that the path is harmless, only that its effect here is small.
Fixing it moves every binding number in the corpus and is out of scope for a
resolution PR; carried on `qou-uicf`.

---

## 5. Verification

- **Lean.** `lean -DautoImplicit=false -s 65536`, `LEAN_PATH` = the restored
  `.lake/packages/*/.lake/build/lib/lean` trees — **exit 0** on both files.
  `#print axioms` on all ten declarations reports `propext` / `Classical.choice` /
  `Quot.sound` and **no `sorryAx`**. `check-sidecars.sh` classifies
  `UICFunctionalSelection` as *"no ℝ, generic OK"* and `UICLogSummandEven` as
  *"archimedean construct present, ℝ justified"*.
- **Probe.** 16/16, `mp.dps = 70`, proton pin (`q_at()`, agreement 7.6e-18),
  convention D recorded, Rust MPFR kernel live — the probe **refuses** without it,
  since the fallback YSN family violates the braid relation.
- **Precision gates.** `scripts/precision-gates.sh --changed` — **exit 0**, and
  **zero hits on either new file**. The eleven contended tree-measuring audit
  witnesses moved and were reverted per `qou-v0t8`.
- **Render QA.** Full preflight grep battery on the edited `.md`: balanced
  `$`/`$$`/`{}`/`\big(`-`\big)`/`\begin`-`\end`; no list-parser hijack inside
  `$$…$$` (one found and fixed); no inner align-family environment in inline
  `$$`; no undeclared unicode outside math; every symbol introduced before use.
  The pipeline render was **not** run separately — the folio-assistant clone at the
  pinned platform `df28d02` was installed and `run-validate` executed; see the PR
  for its result.
