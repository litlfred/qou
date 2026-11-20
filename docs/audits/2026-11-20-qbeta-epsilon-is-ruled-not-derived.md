# Q_β: ε is ruled, not derived — and so are the other two factors

Bean `qou-99qc`. Owner question 2026-11-20: *"Is this true? ε is Markov trace. Don't we need to derive it?"*
This is a status audit. Nothing is wired and no number in the corpus changes. All figures below were measured at the proton pin
(`qou_substrate.constants.q_at()`) at 50 dps, against CODATA Q_β = 0.78233341 MeV.

## 1. Short answer

**ε = Markov trace at z_D is an owner ruling (2026-09-08), not a derivation.** The content block
`nuclear-interactions/neutron-qvalue-symbolic.md` says so in words: *"The functional applied to Δ … is the Markov trace at
z_D (convention D, owner ruling 2026-09-08)."* The ruling picked between admissible options; the 2026-09-05 options doc
(`2026-09-05-qbeta-functional-decision-options.md`, Option C) lists its commitment as *"uniformity of functional across mass
and decay channels — a substantive physical claim, currently unargued."*

ε is not the only posited factor. `Q_β = |ε(Δ)|·E₀` has three, and none is derived:

| factor | status | where it says so |
|---|---|---|
| Δ = net(n) − net(p), from typed crossings uu = σ, dd = σ⁻¹, ud = ½(σ + σ⁻¹) | **definition** | `neutron-qvalue-symbolic.md`: "It is a definition, not a derived result"; Lean `commutant_trace_eq` shows no weight-preserving operator commuting with F₃ separates uud from udd beyond the pivot |
| ε, the functional | **ruling** | as above |
| E₀ = m_e/(q(q−1)) (or the tower-summed /(1−ℏ_q²)) as the MeV-per-unit-trace scale | **posited** | same block: "the derivation of its series is still open"; the dashboard tags α·ln(…) energy forms POSITED (bean qou-mkm8) |

## 2. The grid, re-measured

tr_z(Δ) = h²/2 − h·z (Δ's γ coefficient h²/2, σ₀ and σ₁ coefficients −h/2 each).

| z | tr_z(Δ) | × E₀ (order zero) | × E₀ (tower-summed, canonical since 2026-09-03) |
|---|---|---|---|
| 1 (Form A, inadmissible under D) | −0.187207 | 0.78365 (+0.17 %) | 0.79142 (+1.16 %) |
| q (augmentation) | −0.210199 | 0.87989 (+12.5 %) | 0.88861 (+13.6 %) |
| z_D (ruled) | −0.106236 | 0.44470 (−43.2 %) | 0.44911 (−42.6 %) |

So the remembered 0.17 % needs **two** superseded choices at once: z = 1 *and* the order-zero E₀. With the canonical
tower-summed E₀ the same Form A is +1.16 %.

## 3. The decisive check: Δ is not the difference of the mass-channel objects

If ε and the scale were derived, they would follow from energy conservation, Q_β = m_n − m_p − m_e, with each nucleon mass
from the mass channel. The canonical nucleon mass is m = 2(m_μ·F_Bor − 6 m_e), F_Bor = |tr_M(β)|·[3]_q!/q³, so the
mass-channel scale per unit trace is 2 m_μ [3]_q!/q³ = **945.76 MeV**, against E₀ = 4.186 MeV. Applied to this Δ:

| z | 945.76·\|tr_z(Δ)\| − m_e |
|---|---|
| 1 | 176.5 MeV |
| z_D | 99.96 MeV |

Two to three orders of magnitude off. **The Δ in the Q_β formula is not the difference of the objects whose traces give the
nucleon masses**, and E₀ is not the mass channel's scale. The decay formula is a separate construction that shares q₀ and
H₃(q) with the mass channel but no derivation step. Energy conservation therefore cannot currently be used to *derive* ε:
there is no independently computed neutron mass to subtract — production defines m_n = m_p + Q_β + m_e
(`m_p_substrate_identity_50dps.py:10`), which is circular for this purpose.

## 4. The other corpus route is fitted

`prop:flavor-split-substrate` gives (m_n − m_p)/M_N ≈ (q−1)²(1−q⁻⁴)/3 and hence Q_β = **0.78068 MeV (−0.21 %)** with no ε.
Its own proof, Step 2, labels the per-quark split h²·ℏ_q/√q *"a phenomenological ansatz … selection against the target"*, and
Steps 1 and 3 hold only for the excised convention-C weight. Not a derivation either.

## 5. What a derivation would have to supply

1. **The u/d distinction inside the braid** — the step currently a definition (typed crossings). Without it p and n are the
   same Borromean word and Q_β = −m_e. This is the isospin problem, not a Q_β-specific one.
2. **One functional and one scale for masses and decay.** If (1) gives nucleon words β_p, β_n, energy conservation *derives*
   Q_β = 2 m_μ [3]_q!/q³·(|tr_M(β_n)| − |tr_M(β_p)|) − m_e, with ε = the mass channel's tr_M at z_D. The 2026-09-08 ruling would
   then become a theorem — but the scale would be 945.76 MeV per unit, not E₀, so the trace difference must be ~10⁻³, not ~0.1.
3. **Or** a derivation that the decay channel is a different object (a width functional, per the CAL-2 ruling Q_β = ℏ/𝔇_β),
   with its own functional and scale argued, not chosen.

Route 2 is the one that would make the decay sector parameter-free. It reduces to the u/d problem.

## 6. Reproduce

```python
q = qou_substrate.constants.q_at(); h = q - 1/q; zD = q**3/(q**2+1)
t = h**2/2 - h*z                      # tr_z(Delta)
E0 = m_e/(q*(q-1));  E0_tower = E0/(1-((q-1)/q)**2)
S = 2*m_mu*(q+1/q)*(q**2+1+q**-2)/q**3   # mass-channel scale, m_mu = m_e*Vol(4_1)/hbar_q^2
X = (q-1)**2*(1-q**-4)/3;  Q_fs = m_p*X/(1-X/2) - m_e
```
