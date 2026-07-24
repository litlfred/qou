# The t₅(τ₀) = −10 hauptmodul gate wired as a discrete validator on q₀ ↦ τ dictionary candidates

**Date:** 2026-07-24 · **Bean:** qou-0ytj (W8) · **Axis:** Bring modulus / τ-dictionary
(idea A2's consumer; same spirit as the A3 integer-trace prune) · **Tier:**
scope-(a), audit-only · **Discipline:** NO FIT; nothing wired to production.

**Probe:** [`computations/probes/tau_dictionary_hauptmodul_validator.py`](../../computations/probes/tau_dictionary_hauptmodul_validator.py)
→ [`tau-dictionary-hauptmodul-validator.witness.json`](../../computations/probes/tau-dictionary-hauptmodul-validator.witness.json)
— 5/5 assertions passed, exit 0.
**Gate (upstream, on main):** [`QOU/Archimedean/BringHauptmodulGate.lean`](../../content/quantum-observable-universe/lean/QOU/Archimedean/BringHauptmodulGate.lean)
(exact-rational arithmetic lock) + [`bring_hauptmodul_gate_probe.py`](../../computations/probes/bring_hauptmodul_gate_probe.py).

## The validator contract

Bring's modulus $\tau_0$ is unique only mod $\Gamma_0(5)$ (Riera–Rodríguez 1992
Thm 1: the residual gauge inside $\mathrm{Sp}(8,\mathbb{Z})$ is $\Gamma_0(5)$),
so the invariant coordinate of the modulus is the genus-0 hauptmodul of
$X_0(5)$,

$$
  t_5(\tau) = \bigl(\eta(\tau)/\eta(5\tau)\bigr)^6,
  \qquad t_5(\tau_0) = -10 \ \text{(exact rational)},
$$

with Fricke companion $j(5\tau_0) = 5^3/t_5(\tau_0) = -25/2$. Both $t_5$ and
$\tau \mapsto j(5\tau)$ are $\Gamma_0(5)$-invariant, so **evaluating them at a
candidate $\tau$ tests Bring-class membership directly** — no orbit search, no
precision search, no free parameter.

**What a verdict means.**

| Verdict | Condition | Meaning |
|---|---|---|
| `ill-defined` | $\mathrm{Im}\tau \le 0$ | the map does not produce a point of $\mathbb{H}$ |
| `PASS` | $\lvert t_5(\tau)+10\rvert \le 10^{-3}$ **and** $\lvert j(5\tau)+25/2\rvert \le 1$ | lands on the Bring $\Gamma_0(5)$-class (tolerances match the gate probe; the reference $\tau_0$ is published to 6 d.p. only, so $\sim 10^{-5}..10^{-4}$ residuals are $\tau_0$-truncation-limited) |
| `NEAR` | $10^{-3} < \lvert t_5+10\rvert \le 10^{-1}$ | numerically ambiguous — a higher-precision candidate $\tau$ is required before any verdict |
| `FAIL` | $\lvert t_5+10\rvert > 10^{-1}$ | **refuted-as-stated, scope-(a)**: the map, as stated, does not land on the Bring class |

A `FAIL` is a scope-(a) negative about the *stated map only* — it excludes
that formula as-is, never any categorical ingredient, and never the existence
of a dictionary. A `PASS` is *necessary, not sufficient*: it certifies the
$\Gamma_0(5)$-class only; functorial provenance (the archimedean $\tau$-functor,
`ArchimedeanTauRealization`) remains the open wall.

**q₀-pin independence (STRICT, per AGENTS.md §q₀ anchor convention).** The gate
constrains the **τ side** only — $t_5 = -10$ contains no $q_0$. A candidate
*map* may be stated at the muon pin or the proton pin; the pins differ by
$\sim 1.6\times 10^{-8}$ relative, far below every verdict boundary, and the
probe asserts in-loop that every candidate's verdict is identical across both
pins.

**Validator self-checks (all asserted):** control $t_5(\tau_0) \approx -10$
(residual $1.7\times10^{-5}$, truncation-limited); $\Gamma_0(5)$-invariance
$t_5(\tau_0+1) = t_5(\tau_0/(5\tau_0+1)) = t_5(\tau_0)$ to $10^{-68}$; Fricke
$t_5(-1/(5\tau_0)) = 5^3/t_5(\tau_0) \approx -25/2$ to $10^{-69}$; sensitivity
$t_5(i) \approx 529.5$ (a non-class point fails loudly).

## Composition with the polarization-blindness constraint

The 2026-07-19 result
([`bring-polarized-q-dictionary-endpoint-blindness`](2026-07-19-bring-polarized-q-dictionary-endpoint-blindness.md))
proved that endpoint-anchored period-side q-dictionaries — the only
non-vacuous kind under free reparameterization — are blind to the polarization
data. That constraint acts on the *method class*; this gate acts *pointwise* on
any concrete $\tau$-image. The two compose as independent discrete filters: a
proposed dictionary must (i) carry dictionary-independent content beyond
endpoints (else vacuous / polarization-blind) **and** (ii) land its
$\tau$-image on the $t_5 = -10$ class (else refuted-as-stated). Neither filter
implies the other.

## Candidate enumeration (corpus, 2026-07-24) and verdicts

Corpus-grep (`docs/`, `computations/`, `content/` for the τ-dictionary terms)
finds **exactly one concrete stated $q_0 \mapsto \tau$ map** plus two
already-pruned method classes; the balance of the table is labelled strawmen
demonstrating the validator mechanics (per the task's fallback deliverable).

| Key | Map | Where stated | Tier before gate | Gate verdict (both pins) |
|---|---|---|---|---|
| REF | $\tau_0 = -0.5 + 0.186676i$ (BDH22) | literature reference (control) | exact invariants | **PASS** ($\lvert t_5+10\rvert = 1.7\times10^{-5}$) |
| C1 | **exact nome** $\tau = i\,\lvert\ln q_0\rvert/(2\pi)$ | [`alpha_em_modular_family_probe.py`](../../computations/alpha_em/alpha_em_modular_family_probe.py) (tranche 7, "the corpus's own B1 fibre dictionary"; zero free constants) | caveated working choice; weight families under it already killed | **FAIL** ($t_5 \approx 1.7\times10^{-31}$, $\lvert t_5+10\rvert = 10.0$) — refuted-as-stated, scope-(a) |
| C1n | naive nome branch $\tau = \ln(q_0)/(2\pi i)$ | implicit branch of the standard nome $q = e^{2\pi i \tau}$ ([tau-correspondence](2026-07-18-alpha-em-tau-correspondence.md), caveated) | caveated choice | **ill-defined** ($\mathrm{Im}\tau < 0$ at real $q_0 > 1$) |
| S1 | STRAWMAN $\tau = i \ln q_0$ (canonical rate as modulus) | this probe only — **not a proposal** | strawman | **FAIL** ($\lvert t_5+10\rvert = 10.0007$) |
| S2 | STRAWMAN $\tau = i\,\hbar_q$, $\hbar_q = 1 - q_0^{-1}$ | this probe only — **not a proposal** | strawman | **FAIL** ($\lvert t_5+10\rvert = 10.0004$) |
| S3 | STRAWMAN $\tau = -\tfrac12 + i \ln q_0$ (half-shift mimicking $\mathrm{Re}\tau_0$) | this probe only — **not a proposal** | strawman | **FAIL** ($t_5 \approx -4.678$, $\lvert t_5+10\rvert = 5.32$) |

**Method classes recorded but not point-evaluable** (no pointwise $\tau$-image
to gate):

- Reciprocal power-law dictionaries $t = c/\lvert\lambda\rvert^p$
  ([qt-dictionary-shape](2026-07-18-alpha-em-qt-dictionary-shape.md)) — target
  is Epstein **heat time**, not a modulus; the class was already killed
  scope-(a) on its own grid test. Out of this gate's domain.
- Endpoint-anchored period-side dictionaries
  ([endpoint-blindness](2026-07-19-bring-polarized-q-dictionary-endpoint-blindness.md))
  — a method-class constraint; composes with this gate as above.
- Endpoint-to-distinguished-constant dictionaries
  ([period-qdeformation](2026-07-18-alpha-em-period-qdeformation.md)) — already
  killed scope-(a) (NULL against the pre-stated distinguished list).

## Honest reading

The corpus's one stated concrete dictionary — the exact nome map — was already
known to be fibre-level bookkeeping rather than the archimedean $\tau$-functor
(tranche-7 synthesis: "the needed dictionary IS the archimedean tau-functor").
The gate now makes that quantitative and discrete: the nome map's $\tau$-image
at the substrate lies essentially at the cusp — $t_5 \to 0$ as
$\mathrm{Im}\tau \to 0^+$ along the imaginary axis, and the observed
image $t_5 \approx 1.7\times10^{-31}$ is exactly that cusp-adjacent regime —
nowhere near the Bring class $t_5 = -10$. **Refuted-
as-stated, scope-(a): the map, as stated, does not land on the Bring class.**
This does not refute the τ-identification programme; it hands every future
dictionary proposal a free, parameter-free first hurdle.

All strawman FAILs share a structural cause worth recording (observation, not
a theorem): purely-imaginary $\tau$-images give **real positive** $t_5$
(η-quotient of purely-imaginary arguments is positive real), while the Bring
class needs $t_5 = -10 < 0$ — reaching it requires a nontrivial real part
(cf. $\mathrm{Re}\tau_0 = -\tfrac12$; S3 shows a half-shift alone is
insufficient).

## Standing instruction for future dictionary proposals

**Before proposing any $q_0 \mapsto \tau$ dictionary** (in an audit doc,
content block, probe, or PR description), run

```bash
python3 computations/probes/tau_dictionary_hauptmodul_validator.py
```

with the candidate added to the `candidates` list (both pins), and report the
verdict in the proposal. A `FAIL` proposal may still be *discussed* as a
stepping stone but must carry the refuted-as-stated label; only a `PASS`
candidate may proceed to the functorial-provenance question (which the gate
does not decide). This mirrors the A3 integer-trace prune's role: a discrete
structural filter applied **before** any precision search, per the
formalize-first probe discipline.

## Scope discipline (anti-laundering)

No fit: no candidate was tuned toward $t_5 = -10$; the strawmen are labelled
demonstrations, not proposals; tolerances were pre-stated from the upstream
gate probe. Nothing is wired to production. A `FAIL` here is a scope-(a)
refutation of the stated map only. The $\tau$-identification (α_EM B2) and the
$\tau$-functor construction remain **open**; the gate adds a necessary
condition, not a construction.

## Cross-references

- The gate (exact + numeric): [`BringHauptmodulGate.lean`](../../content/quantum-observable-universe/lean/QOU/Archimedean/BringHauptmodulGate.lean), [`bring_hauptmodul_gate_probe.py`](../../computations/probes/bring_hauptmodul_gate_probe.py)
- Idea A2 (source): [`2026-07-18-uploaded-papers-binding-mass-gap-ideas.md`](2026-07-18-uploaded-papers-binding-mass-gap-ideas.md) §A2
- τ-correspondence + nome caveat: [`2026-07-18-alpha-em-tau-correspondence.md`](2026-07-18-alpha-em-tau-correspondence.md); nome-independence upgrade: [`2026-07-18-alpha-em-involution-type-nome-independent.md`](2026-07-18-alpha-em-involution-type-nome-independent.md)
- Exact nome dictionary (C1's source): [`2026-07-18-alpha-em-modular-family.md`](2026-07-18-alpha-em-modular-family.md), [`alpha_em_modular_family_probe.py`](../../computations/alpha_em/alpha_em_modular_family_probe.py)
- Composing constraint: [`2026-07-19-bring-polarized-q-dictionary-endpoint-blindness.md`](2026-07-19-bring-polarized-q-dictionary-endpoint-blindness.md)
- Killed adjacent classes: [`2026-07-18-alpha-em-qt-dictionary-shape.md`](2026-07-18-alpha-em-qt-dictionary-shape.md), [`2026-07-18-alpha-em-period-qdeformation.md`](2026-07-18-alpha-em-period-qdeformation.md)
- B2 attack plan (where a future PASS candidate would plug in): [`2026-07-24-alpha-em-b2-tau-identification-attack-options.md`](2026-07-24-alpha-em-b2-tau-identification-attack-options.md)
- Shared-τ keystone: [`2026-07-17-alpha-em-keystone-shared-bring-tau.md`](2026-07-17-alpha-em-keystone-shared-bring-tau.md)
