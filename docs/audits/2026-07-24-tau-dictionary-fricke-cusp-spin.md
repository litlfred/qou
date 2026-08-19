# τ-dictionary follow-up: exact cusp factorization, bar ↔ Fricke candidate class, and the A6 spin/sign leg

**Date:** 2026-07-24 · **Bean:** qou-yev9 (W8b + A6) · **Axis:** Bring modulus / τ-dictionary
(follow-up to the W8 hauptmodul-gate wiring) · **Tier:** scope-(a), audit-only ·
**Discipline:** NO FIT; candidates enumerated from structure only, never adjusted toward $-10$;
nothing wired to production.

**Probe:** [`computations/probes/tau_dictionary_fricke_spin_probe.py`](../../computations/probes/tau_dictionary_fricke_spin_probe.py)
→ [`tau-dictionary-fricke-spin-probe.witness.json`](../../computations/probes/tau-dictionary-fricke-spin-probe.witness.json)
— 6/6 assertions passed, exit 0.
**Upstream (this branch):** [`tau_dictionary_hauptmodul_validator.py`](../../computations/probes/tau_dictionary_hauptmodul_validator.py)
+ [`2026-07-24-tau-dictionary-hauptmodul-gate-wiring.md`](2026-07-24-tau-dictionary-hauptmodul-gate-wiring.md)
(W8: the corpus's one concrete dictionary, the exact nome map $\tau = i\,|\ln q_0|/(2\pi)$,
FAILs the Bring gate $t_5(\tau_0) = -10$ with $t_5 \approx 1.7\times 10^{-31}$).
**Sources for Task 3:** BN12 = `library/sigma12-065/sigma12-065.pdf` (Braden–Northover, SIGMA 8 (2012) 065);
BDH22 = `library/arxiv-2208.13692v1/2208.13692v1.pdf` (Braden–Disney-Hogg). Idea ledger:
[`2026-07-18-uploaded-papers-binding-mass-gap-ideas.md` §A6](2026-07-18-uploaded-papers-binding-mass-gap-ideas.md).

The owner asked two follow-ups on the W8 FAIL: **(Q1)** "is there a zero we can factor
out?" and **(Q2)** "is there geometric intuition to exploit?". Answers: Q1 — yes, exactly,
and it is the cusp-$0$ zero of $t_5$ (§1); Q2 — yes, two proved invariants organize the
whole candidate space (sign / half-period twist, and the Fricke-circle modulus $5\sqrt5$),
but every natural bar ↔ Fricke candidate still fails the gate (§2, §3).

## 1. Task 1 — the cusp-factorization identity (exact)

**Theorem-level statement.** From $\eta(-1/\tau) = \sqrt{-i\tau}\,\eta(\tau)$ one gets the
exact Fricke-chart identity for the $\Gamma_0(5)$ hauptmodul
$t_5(\tau) = (\eta(\tau)/\eta(5\tau))^6$: with $\tau' = W_5(\tau) = -1/(5\tau)$,

$$
t_5(\tau) = 5^3\,\bigl(\eta(5\tau')/\eta(\tau')\bigr)^6 ,
$$

so on the imaginary axis $\tau = iy$ (where $\tau' = i/(5y)$, $\tilde q = e^{2\pi i\tau'} = e^{-2\pi/(5y)}$):

$$
t_5(iy) \;=\; 125\,\tilde q\,\prod_{n\ge 1}\frac{(1-\tilde q^{\,5n})^6}{(1-\tilde q^{\,n})^6}
\;=\; 125\,\tilde q\,\bigl(1 + 6\tilde q + 27\tilde q^2 + 98\tilde q^3 + 315\tilde q^4 + 912\tilde q^5 + 2456\tilde q^6 + \cdots\bigr).
$$

The expansion coefficients are **integers** (the 6-coloured-partition series corrected at
levels $5\mathbb{N}$), computed in-probe by exact integer series arithmetic:

$$
c_0,\dots,c_8 \;=\; 1,\; 6,\; 27,\; 98,\; 315,\; 912,\; 2456,\; 6210,\; 14937
\qquad (c_9 = 34390).
$$

At the nome dictionary $y = |\ln q_0|/(2\pi)$ the Fricke chart evaluates to
$\tilde q = \exp\!\bigl(-4\pi^2/(5\ln q_0)\bigr)$, and (mpmath, 120 dps; both $q_0$ pins;
relative agreement of the direct $\eta$-product against the cusp form $\approx 2.5\times10^{-119}$):

| pin | $\tilde q = e^{-4\pi^2/(5\ln q_0)}$ | $t_5(iy)$ (direct $\eta$-product, 35 digits) |
|---|---|---|
| muon | $1.367790030991329745331955\times10^{-33}$ | $1.7097375387391621816649443628211959\times10^{-31}$ |
| proton | $1.367778586487380871575737\times10^{-33}$ | $1.7097232331092260894696716685721023\times10^{-31}$ |

This certifies the parent-session analysis (A) and answers **Q1**: the zero one factors
out is the **cusp-$0$ zero of $t_5$** — $t_5(iy) = 125\,\tilde q\,(1 + O(\tilde q))$ with the
prefactor $125\tilde q$ carrying the entire $10^{-31}$, and the residual factor
$1 + 6\tilde q + \cdots$ equal to $1$ to 32 digits. After factoring, **nothing $-10$-like
remains**: the nome dictionary is a chart at the cusp $0$ of $X_0(5)$, exponentially
cusp-suppressed as an exact statement, not a numeric accident; the Bring class
$t_5 = -10$ is interior. The verdict "refuted-as-stated" is unchanged; the factorization
explains it.

Numeric cross-checks (all asserted): the Fricke product identity
$t_5(iy)\,t_5(i/(5y)) = 125$ at generic $y$ to $3.5\times10^{-68}$; coefficient peel at
moderate $\tilde q$ ($y = 1/2,\ 0.3$) resolving $c_0..c_5$ individually and the
$c_6..c_8$ block against the exact $c_9$ tail bound.

## 2. Task 2 — bar ↔ Fricke candidate class (falsifier-first)

Question: is there a **natural, zero-free-parameter** map from the bar-symmetric nome data
$\{\ln q_0, -\ln q_0\}$ into the τ-plane whose image is Fricke-stable (interior) rather than
cusp-adjacent? Candidates enumerated from bar/Fricke/half-period structure **only** (no
tuning); gated with the committed validator's tolerance ladder at both $q_0$ pins
(verdicts pin-stable, asserted).

### Two proved invariants (the geometric intuition, Q2)

**Sign invariant (half-period / "spin" obstruction).** For real modular nome
$\hat q = e^{2\pi i\tau} \in (-1,0)\cup(0,1)$:

$$
t_5(\tau) = \hat q^{-1} \prod_{n\ge1} \frac{(1-\hat q^{\,n})^6}{(1-\hat q^{\,5n})^6},
$$

and every product factor is strictly positive, so $\mathrm{sign}\,t_5 = \mathrm{sign}\,\hat q$.
Hence $t_5 = -10 < 0$ **requires the odd-nome chart** $\hat q < 0$, i.e.
$\mathrm{Re}\,\tau \equiv \tfrac12 \pmod 1$ — a half-period twist of the nome/θ-frame.
Consequence (structural exclusion with cited invariant, per AGENTS.md §Before declaring
"refuted" (b)): **every purely-imaginary dictionary** — in particular every bar-symmetric
$|\cdot|$-nome map — has $t_5 > 0$ and can never pass the gate. This upgrades the W8
"structural cause worth recording" observation to a proved invariant. (Consistency check:
the Bring representative itself sits on the twisted line, $\mathrm{Re}\,\tau_0 = -\tfrac12$.)

**Fricke-circle invariant.** On the $W_5$-fixed circle $|\tau| = 1/\sqrt5$ the involution
acts as $\tau \mapsto -\bar\tau$; since $t_5$ has real $q$-coefficients,
$t_5(-\bar\tau) = \overline{t_5(\tau)}$, and the functional equation
$t_5(\tau)\,t_5(-1/(5\tau)) = 125$ becomes $t_5\,\overline{t_5} = 125$:

$$
|t_5(\tau)| \;=\; 5\sqrt5 \;\approx\; 11.1803
\qquad \text{on the whole circle } |\tau| = 1/\sqrt5 ,
$$

while the gate needs $|{-10}| = 10 \ne 5\sqrt5$. So **no parametrization of the
$W_5$-fixed circle can ever pass** — a one-line structural prune of the entire
"Fricke-interior locus" family (asserted numerically to $5\times10^{-48}$; at the fixed
point itself $t_5(i/\sqrt5) = +5\sqrt5$ exactly, dev $1.5\times10^{-49}$).

Notably, the circle **does** host the natural bar ↔ Fricke dictionary the question asks
for: $\tau(q_0) = e^{i(\pi/2 - \ln q_0)}/\sqrt5$ satisfies the exact equivariance
$\tau(q_0^{-1}) = W_5(\tau(q_0))$ (asserted to $10^{-45}$) — bar on the $q$-side **is**
Fricke on the τ-side, and the image is interior. It is excluded anyway by the modulus
invariant. Recorded, not interpreted: the two obstructions are complementary — interior
Fricke-natural images have the wrong modulus ($5\sqrt5$), cusp charts have the wrong size
($10^{-31}$), and pure-imaginary images have the wrong sign ($+$).

### Candidate table (all verdicts identical across muon/proton pins)

| Key | Map (zero free parameters) | $t_5$ (muon pin) | $\lvert t_5+10\rvert$ | Verdict |
|---|---|---|---|---|
| N1 | $\tau = i/\sqrt5$ (W₅ fixed point; bar⊗Fricke symmetrization of the nome family) | $+5\sqrt5 = 11.1803\ldots$ (exact) | $21.18$ | **FAIL** |
| N1h | $\tau = -\tfrac12 + i/\sqrt5$ | $-23.108$ | $13.11$ | **FAIL** |
| N2 | $\tau = e^{i(\pi/2-\ln q_0)}/\sqrt5$ (exactly bar↔Fricke-equivariant, interior) | $10.215 - 4.545\,i$ | $20.72$ | **FAIL** |
| N2b | bar partner $e^{i(\pi/2+\ln q_0)}/\sqrt5$ ($= W_5\circ$N2; conjugate $t_5$, asserted) | $10.215 + 4.545\,i$ | $20.72$ | **FAIL** |
| N2h | $-\tfrac12 + $ N2 | $-22.15 + 4.586\,i$ | $12.99$ | **FAIL** |
| N3 | $\tau = i\sinh(\ln q_0)$ (bar-odd split) | $+7.515\times10^{-4}$ | $10.00$ | **FAIL** |
| N3h | $-\tfrac12 + i\sinh(\ln q_0)$ | $-4.697$ | $5.30$ | **FAIL** |
| N4 | $\tau = i\cosh(\ln q_0)$ (bar-even split, $[2]_{q_0}/2$) | $+548.16$ | $558.2$ | **FAIL** |
| N4h | $-\tfrac12 + i\cosh(\ln q_0)$ | $-560.16$ | $550.2$ | **FAIL** |
| N5h | $-\tfrac12 + i\ln(q_0)/(2\pi)$ (spin-twisted W8 nome map; nome $= -1/q_0$ exactly) | $-7.602\times10^{-7}$ | $10.00$ | **FAIL** |

**Honest outcome: 10/10 FAIL; no PASS was found; nothing is proposed.** Two recorded
observations (recorded-not-interpreted, per the task's discipline):

- **N5h** — the half-period ("spin") twist of the corpus's committed nome dictionary has
  modular nome exactly $-1/q_0$ (asserted) and moves $t_5$ from $+1.7\times10^{-31}$ to
  $-7.6\times10^{-7}$: the twist **fixes the sign** (necessary condition of §3 met) but the
  image is still cusp-suppressed — 7 orders below $|{-10}|$ instead of 30. Sign is
  necessary, nowhere near sufficient.
- **N3h** is the closest miss of the enumeration ($t_5 \approx -4.697$, residual $5.30$,
  deep in the FAIL band). Recorded exactly; not adjusted; not a proposal.

The trivial Fricke image of the W8 nome map, $W_5(\tau_{\text{nome}}) = i\cdot 2\pi/(5|\ln q_0|)$,
carries the same $\Gamma_0(5)$ information with $t_5 = 125/t_5(\tau_{\text{nome}}) \approx 7\times10^{32}$
— same class, same FAIL; not tabulated separately.

## 3. Task 3 — A6 sign leg: the printed spin data, verified exactly

All checks are exact (sympy over $\mathbb{Z}$ / $\mathbb{Q}(i, y_0)$) on data **printed** in
BN12/BDH22; nothing numerical is trusted from the briefing.

**The vector of Riemann constants (BN12 Thm 3 = BDH22 Prop 5.13, verbatim cross-paper
agreement, RR92 homology basis).** With base point the order-5 fixed point ($Q$ in BN12,
$a$ in BDH22) and $\tau_B = \tau_0 M_{RR}$,
$M_{RR} = \begin{pmatrix} 4&1&-1&1\\ 1&4&1&-1\\ -1&1&4&1\\ 1&-1&1&4 \end{pmatrix}$,
$\tau_0 = -\tfrac12 + i\,\mathrm{Im}(\tau_0)$:

$$
K_Q \;=\; \tfrac{1}{10}\,(3,\,2,\,-2,\,-3) \;+\; \mathrm{Im}(\tau_0)\,(1,\,-2,\,-2,\,1)\,i .
$$

Verified exactly from the printed data (all asserted in the probe):

1. **The printed order-5 homology action** $M$ (BN12 §5.3, 8×8 integer matrix) satisfies
   $M^5 = \mathrm{Id}$ and $M \in \mathrm{Sp}(8,\mathbb{Z})$ (both symplectic conventions), and its
   Smith normal form is re-derived: $M - \mathrm{Id} = U\,\mathrm{Diag}(1,1,1,1,1,1,5,5)\,V$ —
   exactly as BN12 print. $M_{RR}$: $\det = 125$, spectrum $\{5,5,5,1\}$,
   $5M_{RR}^{-1} \in M_4(\mathbb{Z})$ (the BDH22 Prop 4.4 integrality).
2. **The 2N-torsion property (BN12 Lemma 1, $N=5$) holds and sharpens.** $(1,-2,-2,1)$ is a
   $5$-eigenvector of $M_{RR}$, whence, symbolically in $\mathrm{Im}(\tau_0)$,
   $$
   5\,K_Q \;=\; (4,\,-4,\,-6,\,1) \;+\; \tau_B\,(1,\,-2,\,-2,\,1) \;\in\; \mathbb{Z}^4 + \tau_B\mathbb{Z}^4 ,
   $$
   while $k\,K_Q \notin \Lambda$ for $k = 1..4$ (unique candidate $m = (k/5)(1,-2,-2,1)$
   non-integral): $K_Q$ is **exactly 5-torsion**, sharpening Lemma 1's $2N = 10$ bound.
3. **Internal consistency of BN12's printed chain:** the intermediate
   $2K_Q = \tfrac15(-12,-3,3,-3) + \tau_0\,(-6,-6,3,0)$ (p. 19) is lattice-equivalent to
   $2\times$Thm 3 with explicit integer vectors $n = (-4,1,3,-1)$, $m = (-1,-1,2,-1)$.
4. **τ₀ prints:** BDH22's corrected $\tau_0 = -0.5 + 0.186676i$ passes the $t_5$ gate
   ($|t_5+10| = 1.7\times10^{-5}$); BN12's own 6-d.p. print $0.185576$ does **not**
   ($|t_5+10| = 0.040$). The BDH22 correction is load-bearing for any
   $\mathrm{Im}(\tau_0)$-dependent datum (e.g. the imaginary leg of $K_Q$).

**The unique invariant characteristic — and a correction to the briefing.** The unique
$\mathrm{Aut} = S_5$-invariant theta characteristic is $\Delta = 3a + b - c$ (BDH22 Ex 5.3 +
Thm 5.11; existence already BN12 Thm 4), it is **even** — the parent briefing's phrase
"odd theta-characteristic / spin twist" is wrong on this point — and it equals the Szegő
divisor $\Delta_S$ with $K_a = A_a(\Delta_S)$ (BDH22 Prop 5.13, verified there to
$10^{-118}$). Orbit decompositions: odd $120 = 20+20+20+60$ (Cor 5.7); even
$136 = 1+5+5+5+10+10+10+30+30+30$ (Thm 5.9), the "$1$" being the unique fixed point.

**The S₅-forcing argument (stated; Lean deferred).** $S_5$ permutes the $2^8 = 256$
half-period characteristics with exactly one fixed point (the even orbit "$1$"); therefore
any $S_5$-equivariant assignment of a distinguished characteristic to Bring's curve is
forced onto $\Delta$, and in the θ-frame based at $a$ the invariant spin structure is the
**origin** ($K_a - A_a(\Delta_S) = 0$: the "canonical spin normalization" of idea A6 is the
zero characteristic in the RR92 frame). A Lean lemma for the forcing argument
(unique-fixed-point ⇒ equivariant map lands on it) was **not** attempted this session: the
sandbox Lean environment is cold and restoring it was out of scope — stated honestly, not
machine-checked.

**The formalize-first invariant for dictionaries (what A6 adds).** The discrete datum a
dictionary candidate must carry is a **half-period twist of the nome/θ-frame**: by the sign
invariant of §2, a τ-image can meet $t_5 = -10$ only in the odd-nome chart
$\mathrm{Re}\,\tau \equiv \tfrac12 \pmod 1$ ($\hat q < 0$). Necessary condition, applied to
the Task-2 candidates: exactly the half-shifted variants (N1h, N2h, N3h, N4h, N5h) acquire
$t_5 < 0$ under the twist — all of them do, and none lands on $-10$. Two distinct discrete
data must not be conflated: (i) the nome-frame half-period twist that flips
$\mathrm{sign}\,t_5$, and (ii) the invariant (even) characteristic $\Delta$ that normalizes
the θ-frame origin. The physical identification worldline-spin ↔ Bring spin structure
remains a **framework hypothesis** (A6's own risk note) — nothing here establishes it, and
any future use must ride a conditional class per AGENTS.md §3b-cond.

## 4. Scope discipline (anti-laundering)

- **No fit.** Every candidate is enumerated from bar/Fricke/half-period structure; none was
  adjusted toward the gate; the expansion coefficients are exact integers from the
  η-product; tolerances are the committed validator's pre-stated ladder.
- **Scope-(a) by default.** Every FAIL refutes the *stated map only*. The two (b)-type
  exclusions — pure-imaginary dictionaries (sign invariant) and the $W_5$-fixed-circle
  family ($|t_5| = 5\sqrt5$) — cite proved invariants, as §Before declaring "refuted"
  requires for structural exclusions.
- **Nothing wired.** Audit-only witness; the τ-identification (α_EM B2) and the archimedean
  τ-functor remain open; the gate gains two new necessary conditions (sign/twist;
  not-on-the-Fricke-circle), not a construction.
- **Render-QA:** the preflight grep battery was run by hand (balanced math delimiters,
  no KaTeX-rejected macros, no markdown-list hijack lines inside display math, no inline
  align-family environments); the pipeline render was not run in this sandbox — stated
  explicitly per the render-QA gate: this change was not machine-validated.

## 5. Cross-references

- W8 gate wiring (parent): [`2026-07-24-tau-dictionary-hauptmodul-gate-wiring.md`](2026-07-24-tau-dictionary-hauptmodul-gate-wiring.md)
- The gate (exact + numeric, main): [`BringHauptmodulGate.lean`](../../content/quantum-observable-universe/lean/QOU/Archimedean/BringHauptmodulGate.lean), [`bring_hauptmodul_gate_probe.py`](../../computations/probes/bring_hauptmodul_gate_probe.py)
- Idea A6 (source): [`2026-07-18-uploaded-papers-binding-mass-gap-ideas.md`](2026-07-18-uploaded-papers-binding-mass-gap-ideas.md) §A6
- Nome dictionary (C1's source): [`2026-07-18-alpha-em-modular-family.md`](2026-07-18-alpha-em-modular-family.md), [`alpha_em_modular_family_probe.py`](../../computations/alpha_em/alpha_em_modular_family_probe.py)
- Composing constraints: [`2026-07-19-bring-polarized-q-dictionary-endpoint-blindness.md`](2026-07-19-bring-polarized-q-dictionary-endpoint-blindness.md)
- B2 attack plan: [`2026-07-24-alpha-em-b2-tau-identification-attack-options.md`](2026-07-24-alpha-em-b2-tau-identification-attack-options.md)
- Corpus spin block (no Bring content yet, per A6): [`sign-as-spin-structure.md`](../../content/quantum-observable-universe/quantum-observable-universes/sign-as-spin-structure.md)
