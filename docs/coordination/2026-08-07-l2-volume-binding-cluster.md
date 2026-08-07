# Coordination ledger — L2 / volume-binding cluster

**Owner branch:** `claude/1ppq-l2-closure-attacks-ufrfun` (PR #4664)
**Opened:** 2026-08-07 · **Skill:** `local/coordinate`
**Session beans:** `qou-kemt` + children

---

## 1. Scope map

| PR | Branch | Scope | Rel. to #4664 | Last active |
|---|---|---|---|---|
| **#4664** (mine) | `1ppq-l2-closure-attacks` | L2 attack options; non-EM binding terms; extended Bloch; volume term | — | active |
| **#4610** | `vol-t-he3-snappy-2026-08-02` | `Vol(T)`, `Vol(³He)` of actual braid closures (SnapPy) | **refutes + supplies** | **5 d stale** |
| **#4591** | `tau-mass-complex-volume-2026-08-02` | `Vol + i·CS` census for m_τ | **constrains** | **5 d stale** |
| **#4640** | `copilot/eight-fold` | eightfold honesty pass; **N=2 obstruction proved** | **refutes A2 premise** | active |
| #4617 | Δ_λ/deuteron μ₃ submodularity | same target (Δ_λ magnitude), distinct route | parallel-OK | active |
| #4658 | 5₂ sum rule, Bloch–Wigner caveat | dilogarithm/Bloch | adjacent | active |

---

## 2. Corrections forced on #4664 by siblings

Recorded per skill §6 — **findings are not silently rewritten**; each is an explicit
retraction with its source.

### 2.1 🛑 A2's premise is REFUTED (source: #4640 §2, §4)

My memo §4 claimed *"the eightfold-way chapter independently argues for `N = 3`."*
**That claim is dead.** #4640 shows the chapter was conflating two different `A₂`s:

| | what it is | where from |
|---|---|---|
| `A₂` of `H₃(q)` | Coxeter type of `W(A₂) ≅ S₃`, permutes **strands** | true **by construction** (`Bₙ` has type `Aₙ₋₁`) |
| `A₂ = 𝔰𝔩₃` | flavour SU(3), acts on the **fibre** `V` | needs `dim V = N = 3` |

*"Setting n=3 does not make N=3"* — and the framework gives **`N = 2`**.

Worse for A2, #4640 §4 **proves** (sorry-free, scope-(b), invariant cited = Schur–Weyl
row cap) that `N = 2` **cannot host** the decomposition: `dim V_{(1³)} = C(N,3)`
vanishes iff `N < 3`; at `N=2`, `8 = 4+4+0` — no singlet, no η′, and *"no choice of q
restores it."*

**Net:** A2 was "test whether binding should use the flavor sector's `N=3`." There is
no flavor `N=3` to import — the framework gives `N=2`, and `N=2` provably cannot host
the octet. That is a **proved open contradiction** (bean `qou-8pl3`, "N=3 routes"), not
a lever available to binding. **A2 → closed as premise-refuted.** The ROAST called it
"near-fatal"; it is now simply dead.

### 2.2 🛑 Hyperbolicity — ESCALATION, not a silent rewrite (source: #4610)

Owner granted caveat 1 this session ("assume it is there and work from there").
**A sibling has already measured it, and the answer is reading-dependent:**

- **Reading 1 — the literal mass-braid `H₉` closures** (`atom_braid_word_3A`):
  **NON-HYPERBOLIC.** SnapPy finds no positively-oriented triangulation under any of
  three averaged-crossing conventions ⇒ **`Vol(T) = Vol(³He) = 0`**. *"The mass-braid
  closure carries no hyperbolic volume."*
- **Reading 2 — corpus-canonical binding links** (SDP registry): `T → 8₁₁`,
  `³He → L6a4 = Borromean`. Both SnapPy-verified **hyperbolic**.

So the owner's grant is **sound under Reading 2 and false under Reading 1**. Escalated
to the author on #4664 rather than picking a reading myself — which reading is
canonical for *binding* is exactly the question, and choosing it to keep my route
alive would be the fit this arc keeps catching.

### 2.3 🛑 `Vol(𝓑₃)` is NOT a per-nucleon volume (source: #4610 Reading 2)

My §5b treated `Vol(𝓑₃) = 7.3277` as the **per-nucleon** volume ("the framework's
nucleon *is* the Borromean link"). The corpus-canonical registry assigns the Borromean
link `L6a4` to **³He — an A=3 isotope**, not a single nucleon. The per-nucleon reading
is withdrawn; §5b's `1.966×` and the factor-2 discussion are recomputed below against
the actual per-isotope assignment.

### 2.4 ⚠️ The CS leg is calibration-blind (source: #4591)

My caveat 2 asked "why would real binding pick up `CS` rather than `Vol`?" #4591 gives
a sharper and more damaging answer: **the muon anchor is CS-blind.** `CS(4₁) ≈ 0`
(figure-eight is amphichiral), so the anchor fixes **no** CS-dependence — *"any
`F(Vol, CS)` reducing to `Vol` at `CS = 0` is equally muon-consistent — a whole
function's freedom."*

**Consequence for the extended-Bloch route:** introducing `CS` as a *magnitude* adds an
unconstrained functional degree of freedom that the calibration cannot check — the same
fit-smuggling in new costume. **The `Vol` leg is unaffected.**

*Distinction worth preserving:* #4591 searches over a free functional `F(Vol, CS)`;
my use of the extended Bloch group is to **fix an integer flattening** from the gluing
equations — that *removes* freedom rather than adding it. So the flattening role
survives; a **CS-carrying magnitude does not**. Route narrows to `Vol` + canonical
flattening.

---

## 3. 🛑 RETRACTION — §3 below is NOT a new result; it re-derives an existing corpus law

**Corpus-grep failure, mine.** Before claiming §3 I did not grep for an existing
volume–binding law. There is one:

- [`computations/a3_mirror_residual_reconciliation.py`](../../computations/a3_mirror_residual_reconciliation.py) L59–64:
  `B_T_bc = M_E * 2 * VOL_8_11`, `B_He3_bc = M_E * 2 * VOL_L6a4` — i.e. the corpus
  already carries **`B = 2·m_e·Vol(K)`** as the *bond-count* binding law.
- [`computations/b_over_a_v5_unified.py`](../../computations/b_over_a_v5_unified.py) L327:
  *"Kashaev law `B = ρ_F · m_e · Vol_hyp(K)`; historical knot IDs (6₂, 8₁₁, L6a4)."*

My `E₀·Vol/B ≈ 3.97–4.09` is **algebraically the same statement**: `E₀ = m_e/(q₀(q₀−1))
= 8.1918·m_e`, so `E₀·Vol/B ≈ 4` ⟺ `B ≈ 2.05·m_e·Vol` — the existing factor-2 law with a
2.4 % offset. The mirror-pair ratio observation then follows trivially from it.

**What actually survives as mine:** only the narrower observation that #4610's
refutation is of **`tr_M` specifically**, and that the *already-existing* pure-`Vol`
law does better on the mirror pair than `Vol·tr_M` does. That is a useful pointer for
#4610, and it is much smaller than §3 as first written.

This is the AGENTS.md #1515/#1532/#1543 pattern (declare-new-against-corpus) committed
by the agent who quoted the rule two documents ago. Recorded, not buried.

**The corpus also already recorded the honest negative I was walking toward**
([`binding_link_volumes.py`](../../computations/binding_link_volumes.py) header):
`B = m_e·Vol(K_bind)·Δtr` gives **−60 % for both ³H and ³He**, and *"the A-dependence
cannot live in a single binding-link volume."*

## 3b. The original §3 text (retained for the record, now downgraded)

#4610 concludes *"`ρ = tr_M` radial handle refuted under every volume reading."*
Correct — but their data also shows **what to drop**. Testing the A=3 mirror pair with
**volume alone, zero free parameters** (the overall constant cancels in the ratio):

| quantity | value |
|---|---:|
| `B(T)/B(³He)` (AME2020) | **1.0990** |
| `Vol(T)/Vol(³He)` (#4610 SnapPy) | **1.1308** |
| ratio-of-ratios | **1.0290** → **2.90 % miss** |
| #4610's `Vol·tr_M` prediction | **0.570** vs `C_knot` ratio **1.350** — **anti-correlated** |
| `E₀·Vol/B`: ³He | 3.9743 |
| `E₀·Vol/B`: T | 4.0895 (spread **2.90 %**) |

**Reading:** the refutation in #4610 is a refutation of **`tr_M`**, not of volume.
Dropping `ρ` entirely and using **pure `Vol`** gets the mirror-pair ratio to **2.90 %
with no free parameter**, where `Vol·tr_M` lands on the **wrong side of 1**. The single
overall constant is `≈ 4` for both isobars.

**Discipline flags (stated, not buried):** this is a **two-point** observation on one
mirror pair; `≈ 4` is a constant fitted to two numbers and means nothing until it holds
across `D / T / ³He / ⁴He`; and it is scratch float64, **not witness-grade**
(NO-FLOAT64). The *ratio* claim is the parameter-free part and is the only part worth
anything yet.

---

## 4. Actions taken

- **#4664** — escalation posted (§2.2); memo corrected for §2.1, §2.3, §2.4.
- **#4610** — intent + the §3 volume-only finding posted; **takeover proposed** (5 d
  stale; its own body says *"Lean witness + audit doc to follow"* — never landed).
- **#4591** — intent posted; **takeover proposed** (5 d stale; test plan has 2
  unchecked items: full ≤12-crossing census run + audit doc).
- Beans: `qou-fvzm` (A2) → closed as premise-refuted with #4640 cited.

## 5. Next non-overlapping task

Recompute the volume-binding relation across **all four** L2 binding targets
(`D`, `T`, `³He`, `⁴He`) under Reading 2, ratio-only, zero free parameters — the two-point
`≈4` constant is not evidence until it survives four points. Blocked on the author's
Reading-1-vs-Reading-2 ruling (§2.2).

---

## 6. Reading 1 vs Reading 2 — full pros/cons (author asked for context before ruling)

**Key fact settled by grep:** Reading 2's link assignment is **SDP-derived, not
chosen**. [`binding_link_volumes.py`](../../computations/binding_link_volumes.py)
header: *"BINDING LINKS (from `binding-k-solver.witness.json` **SDP registry**)"* and,
of the ³He→Borromean identification, *"**This is an identification, not a fit.**"*
So the "Reading 2 is a lookup table someone tuned" worry is **unfounded**.

| | **Reading 1** — literal mass-braid `H₉` closures | **Reading 2** — SDP-registry binding links |
|---|---|---|
| **Derivation status** | The framework's **own canonical construction** (`atom_braid_word_3A`). No assignment step to justify. | **SDP solver output**, explicitly "an identification, not a fit." |
| **Hyperbolic?** | **No** — Vol ≡ 0 under all 3 crossing conventions (torus/satellite signature) | `T`→8₁₁ ✓, `³He`→L6a4 ✓ … **but `²H`→Hopf L2a1 is Seifert-fibred, Vol = 0** |
| **Internal check** | — | L6a4 **is** the Borromean link = the per-nucleon braid `𝓑₃`. Non-trivial coincidence. |
| **Consequence for the extended-Bloch route** | **Fatal.** No hyperbolic structure ⇒ no ideal triangulation ⇒ no flattening ⇒ no `β̂`. | Live for `A=3`, **dead for the deuteron**. |
| **Known corpus negative** | — | `B = m_e·Vol·Δtr` gives **−60 % at both ³H and ³He**; *"the A-dependence cannot live in a single binding-link volume."* |
| **Hidden cost** | none — it is what it is | binding link ≠ mass braid, so **"why does binding see the SDP link?"** becomes its own open derivation |

### The problem neither reading escapes

**The deuteron has `Vol = 0` under both.** Reading 1: everything is Vol 0. Reading 2:
`²H → Hopf`, Seifert-fibred, Vol 0. The corpus's +0.2 % deuteron match was obtained by
**substituting `Vol(𝓑₃)` for `Vol(Hopf)`** — an unjustified substitution, and precisely
the move that needs a derivation rather than a convention.

Since `B_D` is the **loosest** of the four L2 binding targets (4.5 ppb), a route that
cannot reach the deuteron at all is not a route to the L2 binding targets.

### Assessment

- **Reading 1** is the *honest* reading (no assignment step) and gives a clean
  **negative**: the mass-braid closure is Gromov-norm 0, so binding is **not** a
  hyperbolic volume of the mass braid. That is a real, publishable structural result
  and it closes the extended-Bloch route for light nuclei.
- **Reading 2** is *also* derivation-legal (SDP output), keeps `A=3` alive, and has the
  L6a4 = `𝓑₃` coincidence in its favour — but inherits the deuteron `Vol=0` hole and a
  recorded −60 % negative at `A=3`.
- **"Both, different objects"** is the most defensible and the corpus's implicit
  position — but it owes a derivation of *why binding sees the SDP link and mass sees
  the `H₉` closure*. That derivation does not exist. Until it does, picking Reading 2
  because it keeps a route alive is a choice, not a result.

**Recommendation:** rule **Reading 2** for `A ≥ 3` work *and* open the deuteron
`Vol(Hopf)=0` substitution as an explicit blocker bean — do **not** let the `𝓑₃`
substitution stand unexamined. Expect the honest outcome to be that volume alone
carries the *ratio* structure (mirror pair, 2.9 %) but **not** the `A`-dependence,
exactly as `binding_link_volumes.py` already found.
