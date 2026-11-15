# D-H3: is the weak vertex proportional to the left projector?

Bean `qou-hlx7` (epic `qou-qs0e`). Branch `claude/weak-vertex-left-projector-2026-11-15`.
Stream 9a, continued in a project thread after the original session stood down.

**Owner decision D-H3 (2026-11-15, relayed by the coordinator):** record *"the weak
vertex is proportional to the left projector"* as an open conjecture, AND try to derive
it. It stays labelled a conjecture until it is proved.

## 0. Short answer

- **Derived at the level of one crossing.** The vertex insertion `W − σ` equals
  `−(q − q⁻¹)·P_L` exactly (`weakVertex_sub_letter`). This holds for every `q` with
  `q ≠ 0` and `q + q⁻¹ ≠ 0`, in both regimes `|q| > 1` and `|q| ≤ 1`.
- **Not true for the weak knot.** Under convention D, the closure of `(σ₁σ₂)⁵`, which is
  T(3,5), has a nonzero right-line part: `τ_D((σ₁σ₂)⁵ P_R) = −q²/(q² + 1)³`. That is a
  share of `−9.33 %` of the knot's trace at the proton `q₀`. This is an exact negative
  for that reading.
- **What the derivation uses.** It uses two inputs that are already in the corpus and
  nothing else:
  - the owner-ruled `leftLine`;
  - the one-sided vertex `weakVertex`, which acts as `σ⁻¹` on the left line and as `σ`
    on the right line.

  Those two definitions already fix the side. The derivation makes that explicit; it
  does not add a new input.

## 1. Inputs

| input | where | status |
|---|---|---|
| letter `σ`: `σ² = hσ + 1`, `h = q − q⁻¹` | `HelicityCommonSource.lean` | definition |
| `leftLine q σ`: the eigenline where `σ` acts with eigenvalue of modulus `> 1` | `LeftLineDefinition.lean` | owner ruling, 2026-11-15 |
| `weakVertex q σ`: the one-sided flip (`W_L` if `|q| > 1`, otherwise `W_R`) | `LeftLineDefinition.lean` | definition |
| uniqueness: an element is fixed by its action on the two lines | `OneSidedWeakVertex.eq_of_eigen_action` | proved |

## 2. Results (Lean)

File: `QOU/QuarkState/WeakVertexLeftProjector.lean`. Base ring: an ordered field `K`
(the left line needs an absolute value) and a generic `K`-algebra `A`. No `ℝ`.

| claim | lemma |
|---|---|
| `W = σ⁻¹·P_L + σ·P_R` | `weakVertex_eq_split` |
| **`W − σ = −(q − q⁻¹)·P_L`** | **`weakVertex_sub_letter`** |
| `(W − σ)·P_R = 0`: the right line does not couple | `insertion_mul_rightLine` |
| `(W − σ)·P_L = −(q − q⁻¹)·P_L` | `insertion_mul_leftLine` |
| `W − σ = 0 ⇔ q − q⁻¹ = 0`, when `P_L ≠ 0` | `insertion_eq_zero_iff` |
| for `x = a + bσ`: `x·P_R = 0 ⇔ x ∈ K·P_L` | `one_sided_iff_smul_leftLine` |
| `\|q\| > 1`: `qσ − q⁻¹σ⁻¹ = (q − q⁻¹)(q + q⁻¹)·P_L` | `skein_eq_leftLine` |
| `\|q\| ≤ 1`: the same weighting gives `P_R` | `skein_eq_rightLine` |
| **label-free:** if `t ∈ {q, −q⁻¹}` and `\|t\| > 1`, then `tσ − t⁻¹σ⁻¹ = (t − t⁻¹)(t + t⁻¹)·P_L` | **`skein_dominant_root`** |
| `\|q\| > 1`: skein difference `= −[2]_q·(W − σ)` | `skein_eq_neg_bracket_insertion` |

Reading of the table:

1. **One-sided and proportional are the same statement inside one letter.** The letter
   algebra `K[σ]` is `K·P_L ⊕ K·P_R`. So an element that kills the right line is a
   multiple of `P_L` (`one_sided_iff_smul_leftLine`). The content of D-H3 at this level
   is therefore *which* line is killed, and that is the owner's `leftLine` ruling.
2. **The skein-weighting caveat is closed.** `force-knot-identification` §III says that
   which crossing carries the weight `q` is a convention. `skein_dominant_root` shows the
   following. Weight the positive crossing by its own dominant eigenvalue, the one of
   modulus `> 1`, whichever root label that is. Then the skein difference is a multiple
   of `P_L`. Under the ruling, the weighting convention and the left line are one choice,
   not two.
3. **Classical limit.** At `h = 0` the insertion vanishes (`insertion_eq_zero_iff`), so
   the left/right distinction exists only off `q² = 1`. This matches
   `oneSidedL_eq_oneSidedR_iff`.

## 3. Beyond one letter: the weak knot T(3,5) (probe)

Probe: `computations/probes/weak_knot_left_line_split_probe.py`. It is exact in sympy
with symbolic `q`, then evaluated with mpmath at 70 digits at the proton `q₀`. No witness
is written. All 21 checks pass.

The probe works in `H₃` through its three Wedderburn blocks. Convention D has weights
`y₍₃₎ = (q⁴+1)/(q²+1)²`, `y₍₂,₁₎ = q²/(q²+1)²` and `y₍₁³₎ = 0`. Let `β = (σ₁σ₂)⁵`, and
split along the two lines of `σ₁`, with `P_L = P₊` at `q > 1`
(`leftLine_eq_Pp_iff`).

| quantity | exact | at `q₀` |
|---|---|---|
| `τ_D(β)` | `q²(q¹² + q⁸ − 1)/(q² + 1)²`, the corpus `W(q)` (bean `qou-egvf`), reproduced | `1.187480613146` |
| `τ_D(β P_L)` | `q⁴(q⁴ + q² + 1)(q⁸ + q² − 1)/(q² + 1)³` | `1.298274553623` |
| `τ_D(β P_R)` | **`−q²/(q² + 1)³`** | `−0.110793940477` |
| right-line share | | `−9.330 %` |
| `τ_D(β P_L) / τ_D(β P_R)` | `−q⁴·[3]_q·(q⁸ + q² − 1)` | |

More detail on the right-line part:

- The letter `σ₂` gives the same `τ_D(β P_R)`.
- The sign block has weight zero, so the right line is seen only through the `(2,1)`
  block.
- Over the family T(3,N), `τ_D((σ₁σ₂)^N P_R)` repeats with period 3 in `N`, because
  `σ₁σ₂` has order 3 on the `(2,1)` block. Its values are `−q⁴/(q²+1)³`,
  `−q²/(q²+1)³` and `q²/(q²+1)²`. None is zero. At `N = 3k` it equals `τ_D(P_R)`.

**Verdict.** The reading "the weak knot's trace is supported on the left line" is
false. This is an exact computation, not a numerical miss. What it excludes is that
reading, for this knot, under convention D. It says nothing against the one-crossing
statement of §2, which is proved. It also says nothing about traces other than
convention D.

How it relates to stream 11 (#7867): there, convention D weighs the two lines `[3]_q : 1`
at every `n`. Here the same `[3]_q` appears as a factor of the T(3,5) ratio. Both say the
trace sees the right line with nonzero weight.

## 4. What is and is not established

- **Established (proved):** D-H3 at the level of one crossing, in the form
  `W − σ = −h·P_L`. This is relative to two corpus definitions, the ruled `leftLine` and
  `weakVertex`.
- **Established (exact negative):** the T(3,5) convention-D trace is not supported on the
  left line.
- **Not established:** that `weakVertex` is the physical weak coupling. That claim
  belongs at the comparison boundary (scope a), and no mathematics here bears on it.
- **Not attempted:** the multi-letter vertex with an `SU(2)` doublet (stream 11's `n ≥ 4`
  corner `sl₂`, #7867). In one letter, flavour and chirality share a 2-dimensional space
  (`FlavourDoubletOnLeftLine.lean`), so the Standard-Model form `T± ⊗ P_L` cannot be
  built there.

## 5. Owner decision: how to record D-H3

The question was posted to the owner as a decision card on 2026-11-15.

1. **Proposition plus the knot negative (recommended, judgement).**
   - What it means: a proposition content block, backed by the Lean above, states the
     one-crossing identity. Its text also records that T(3,5) is not left-supported.
   - Cost: one `.ts`/`.md` pair and a manifest line.
   - Risk: none to any number.
   - Commits to: dropping the "conjecture" label, because the statement it named is
     proved.
2. **Keep it a conjecture.** As first decided, with the Lean cited for the one-crossing
   case. Risk: a reader sees a proved statement labelled open.
3. **Audit and bean only.** No content block.

**Default (no answer):** nothing goes into content. The audit, the bean and the Lean
file are on the branch, and no PR is opened without the owner's go.

## 6. Owner decisions 2026-11-15, after §5

The owner chose **1** (a proposition block plus the knot negative). The owner then also
chose routes **1 + 2** to resolve the knot negative, and added route **4**.

- **Route 1, two levels.** The proposition `prop:weak-vertex-left-projector` is in
  `predicted-spectra`, with its proof block. One sentence in `force-knot-identification`
  §III now says two things: under the `leftLine` ruling, the weighting choice and the
  left line are one choice; and the one-sidedness holds at a crossing, not for the
  T(3,5) trace.
- **Route 2, the exact obstruction.** File `QOU/QuarkState/RightLineTraceObstruction.lean`
  (lean-direct exit 0; axioms `propext`, `Classical.choice`, `Quot.sound`). Let
  `τ = y₃χ₍₃₎ + y₂₁χ₍₂,₁₎ + y₁₁₁χ₍₁³₎` be a block-weighted trace on `H₃` and assume
  `[3]_q ≠ 0`. Then `τ(x P_R) = 0` for every `x` holds iff `y₂₁ = y₁₁₁ = 0`
  (`kills_right_iff`). With `τ(1) = 1`, that trace is the augmentation
  (`normalised_eq_augmentation`).
  - The proof of necessity evaluates `τ` on the images of `1` and `σ₂` only. It does not
    use Wedderburn.
  - The obstruction is the `(2,1)` block. `[3]_q` appears as the determinant of the two
    conditions.
  - The trace ruling is not reopened: the owner ruled `z_D` on 2026-09-08. Switching to
    the augmentation in order to recover one-sidedness would be selection against a
    target.
- **Route 4, the bias for every n.** In progress. It builds on stream 11's
  `ConventionDLineWeights.lean` and seminormal probes (#7867).

## 7. Route 4: the right-line share of torus words, for every n

Probe: `computations/probes/torus_word_right_line_share_probe.py` (121 checks pass). It is
exact, with `Fraction` arithmetic at `q = 11/10` and `q = 3/2`, for `n = 2, …, 7`. The
numbers at `q₀` are mpmath at 70 digits. No witness is written.

The seminormal matrices follow stream 11's `corner_doublet_vs_flavour_probe.py`. The
probe re-checks the Hecke and braid relations itself.

**Setting.**
- `c = σ₁σ₂⋯σ_{n−1}`, so the closure of `c^N` is `T(n,N)`.
- `P_R = (q − σ₁)/[2]_q` is the right line of the first letter, for `q > 1`.
- Convention D gives weight `y₍ₙ₋ₖ,ₖ₎ = [n−2k+1]_q/[2]_qⁿ` to the two-row shapes and
  weight 0 to every shape with three or more rows.

**Results.**

| statement | status |
|---|---|
| The full twist `cⁿ` acts on block `λ` by `q^{2c(λ)}`, where `c(λ)` is the content sum | checked exactly for n ≤ 7 (a standard fact, cited) |
| `τ_D(c^{mn+r} P_R) = Σ_λ y_λ q^{2m c(λ)} g_λ(r)`, with `g_λ(r) = tr_λ(c^r P_R)` and `g₍ₙ₎ = 0` | exact, n ≤ 7, m ≤ 2 |
| `N = 0`: `τ_D(P_L) : τ_D(P_R) = [3]_q : 1` | stream 11's result, reproduced for n ≤ 7 |
| `N = 1`: the share is `−1/(q²(q² + 1))` for every n | exact, n ≤ 7. It follows from the Markov property: `τ(σ₁P_R · σ₂⋯σ_{n−1}) = τ(σ₁P_R)·z_D^{n−2}` |
| The right part is nonzero for every `N ≤ 3n` | exact at both rational `q`, n ≤ 7 |
| `c(n) − c(n−1,1) = n` | arithmetic |
| The hook term `g₍ₙ₋₁,₁₎(r)` vanishes exactly for `r ∈ {2, …, n−2}` | observed, n ≤ 7, both `q`. Not proved |

**The bias theorem, as far as it is established.** For `q > 1` the right-line share of
`T(n,N)` under convention D is `O(q^{−2N})`, at every n. The argument has three steps:
1. The trivial block carries none of `P_R` and has the largest twist, `q^{2c(n)}`.
2. Among the other shapes, the hook `(n−1,1)` has the largest twist, `n` content units
   below the trivial block.
3. So each full twist (`N ↦ N + n`) shrinks the share by at least `q^{−2n}`.

The rate `q^{−2N}` is attained on the residues `r ∈ {0, 1, n−1}`. On the residues where
the hook term vanishes, the decay is faster. The share is never exactly zero for the `N`
tested. So:
- **at N = 0** the bias is `[3]_q : 1` (stream 11);
- **at N = 1** the share is `−1/(q²(q²+1))`, the same for every n (`−0.36364` at `q₀`);
- **for long torus words** the bias grows without bound: the words become left-supported
  only in the limit, at rate `q^{−2}` per power of `c`.

**What rests on what.**
- The twist eigenvalue `q^{2c(λ)}` and the Wedderburn decomposition are cited. The probe
  checks the twist exactly for n ≤ 7 but does not prove it for every n.
- The `O(q^{−2N})` bound is then elementary. Each block's `c` is diagonalisable with
  eigenvalues of modulus `q^{2c(λ)/n}`, because its minimal polynomial divides `xⁿ − z`.
- `n = 3` is fully in Lean (`twist`, `tau_torus_PR_periodic`).
- Nothing here bears on whether any physical quantity is such a long-braid limit. Stream
  11 §6.2 found that no current observable is (scope a). For T(3,5) at `q₀` the share is
  still `−9.33 %`.

**Numbers at `q₀`.** These are the right-line shares from the probe; the first entry of
each row is `N = 0`.
- n = 3: 0.2473, −0.3636, −0.2131, 0.1718, −0.1488, −0.0933, 0.1093
- n = 5: 0.2473, −0.3636, −0.1309, −0.0933, −0.1176, 0.1567, …, `N = 10`: 0.0743
- n = 7, `N = 14`: 0.0413
