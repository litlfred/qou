# Route L: an additive log-trace energy for β decay

Bean `qou-99qc`. PR #8693. Owner selected route L (2026-11-21) after P1/P4 (#8681), P2 (#8680)
and P3 (#8682) all stopped at one wall: the mass channel `E ∝ |tr|·[N]_q!/q^N` is multiplicative
on split and connected-sum words, so it is not an energy balance. Route L asks for an additive
energy functional. Pre-registration: `computations/probes/beta_additive_logtrace/PREREGISTRATION.md`
(committed first, `9ce0a5fef8`). Lean: `QOU/QBeta/LogTraceAdditiveEnergy.lean`. Probe and witness:
`computations/probes/beta_additive_logtrace/` (15/15, exact in ℚ(q), 70 dps, proton q₀). Nothing
is wired. CODATA appears only as a comparison row.

## 1. Answer

1. **The functional exists, and it was already in the corpus.** `E_κ(X) = κ·log|tr X|` is the
   binding channel `B_sym = α·ln(tr_free/tr_atom)` with `α = E₀ = m_e/(q₀(q₀−1))`
   (`docs/audits/2026-06-16-b-sym-linear-chain-closed-form.md`, `QOU.BraidKnot.BsymLinearChain`,
   `QOU.Mass.ChainTraceFactor.neg_log_prod`). Route L applies that channel to the β-decay words.
   Two things follow from that:
   - Its sign is fixed by the corpus as `B = −α log μ`, i.e. a state energy `+α log tr`.
   - Its free-energy reading has no energy spectrum (`QOU.Mass.FreeEnergySigned`).
2. **Additivity is proved where the trace is multiplicative.**
   - One-strand joins, **unconditional**: `logEnergy_tr_mul_adjoin_gen`, from
     `tr_mul_adjoin_gen`.
   - Disjoint blocks, **conditional** on the unproved `TowerSpan`:
     `logEnergy_disjoint_of_towerSpan`.
   - On a word that does not factorise, the defect is `κ·log|tr W/(tr a·tr b)|`
     (`crossTerm_eq_log_ratio`).
   - The identity strand (the ν̄) has log-energy 0 for every κ (`logEnergy_one`). The
     `[N]_q!/q^N` strand factor gave it 95 MeV in P2.
3. **κ is not fixed by the corpus.** Additivity holds for every κ, so it cannot select a scale
   or a sign. Specifically:
   - `α = E₀` is a named normalisation, not a derivation.
   - The volume conjecture cannot supply κ. It is a statement about the coloured Jones
     polynomial at `e^{2πi/N}` as `N → ∞`, not about the fundamental Markov trace at real q₀.
     The corpus itself calls it "τ-side naming, not a derivation input"
     (`skein-mass-relation-proof`).
   - It also fails on these knots. `Vol(3₁) = Vol(unknot) = 0`, but `log|tr(3₁)| = −0.16425`
     while `log|tr(unknot)| = 0`. So no κ makes `κ·log|tr_M(q₀)|` proportional to `Vol` across
     the trefoil and the unknot.
4. **P3's sign problem is NOT fixed by the log.** For the index character,
   `log χ = writhe·ln q`. The p-over-n shift (`+2 ln q`) and the electron (`+3 ln q`) have the
   same sign. So no κ makes the proton lighter while giving the electron positive energy
   (`no_kappa_for_index_character`, scope (b), invariant: the sign of `ln q` for `q > 1`).
5. **On the Markov trace the signs separate, but in the direction opposite to the corpus.**
   The P2 words satisfy `0 < t_e < 1` and `t_n < t_p·t_e` exactly at q₀
   (`t_n = 0.475134`, `t_p·t_e = 0.534002`). Under those hypotheses `markov_log_signs` gives:
   decay balance `Q > 0` iff `κ < 0`, and `E(e⁻) > 0` iff `κ < 0`. The two orderings agree with
   each other, and both need `κ < 0`. The corpus binding sign is `κ = +E₀ > 0`. **Under the
   corpus sign, β⁻ is endothermic and the electron has negative energy.**

## 2. Numbers (witness `beta-additive-logtrace.witness.json`)

E₀ = 4.18598136 MeV, E₀_tower = 4.22748336 MeV, ln q₀ = 0.10434072, CODATA Q_β = 0.78233341 MeV.

### 2.1 Split decay (P2 words: nuc11 p, n; e⁻ = σ₀³; ν̄ = identity)

`Q/κ = log t_n − log t_p − log t_e = −0.116803532`. The argument is the exact rational function
`t_n/(t_p t_e)`, recorded in the witness. As q → 1, `Q/κ → ln 2`: every trace tends to 1/2, so the
electron's −ln 2 dominates.

| κ | Q (MeV) | vs CODATA |
|---|---|---|
| +E₀ (corpus sign) | −0.48894 | wrong sign |
| −E₀ | +0.48894 | −37.5 % |
| −E₀_tower | +0.49378 | −36.9 % |
| needed | −6.69786 MeV = −13.107 m_e = −1.6001 E₀ | comparison only |

Nucleon-only row, for comparison: `(E(n) − E(p))/κ = −0.281057`. At κ = −E₀ that is
+1.17650 MeV, against CODATA m_n − m_p = 1.29333 MeV (−9.0 %). **This row is not evidence for
κ = −E₀.** Three reasons:
- that sign contradicts the corpus convention;
- nuc11 fails the reading-3 confinement SDP (AGENTS.md, `qou-99qc`);
- choosing a sign because it lands near CODATA is selection against the target.

### 2.2 P1 wrapping words (H₆, β_Bor ⊗ photon pair, bridge letters)

The log cross term is `C_log = log|tr W/(tr β · tr Γ · tr bridge)|`.

- **Exactly 0** for W0, W1, W1², W2 and W2b (R = 1 in ℚ(q)). With Γ = 1, W4b is also 0.
- **Non-zero:**

  | word | C_log | κ·C_log at +E₀ |
  |---|---|---|
  | W3 | +1.6348·10⁻⁴ | 6.84·10⁻⁴ MeV |
  | W4 = W6 | +4.5860·10⁻⁵ | 1.92·10⁻⁴ MeV |
  | W7 | −0.090278 | −0.3779 MeV |
  | W4b (Γ = β_Bor only) | −1.1694·10⁻³ | — |

- **Every R → 1 as q → 1.** The interaction is purely a q-deformation effect.
- Exact closed forms are in the witness. Example, W3:
  `R = (q²+1)(q¹²−4q¹⁰+2q⁸−3q⁶+2q⁴−3q²+1) / ((q⁴+1)(q¹²−3q¹⁰+2q⁸−4q⁶+2q⁴−3q²+1))`.

### 2.3 P2 family D (full twist on ≥ 2 nucleon strands, then trefoil and ν̄ clasp)

These are entangled final states. The balance is `Q/κ = log t_n − log|tr W|`.

- **t = +1 words:** Q/κ runs from −0.645 to −1.309.
- **t = −1 words:** Q/κ runs from +0.370 to +0.918.
- **So the sign of Q is set by the chosen twist sign**, which is a chosen linking letter (P2
  §0.5). At κ = +E₀, the t = −1 words give Q from +1.55 to +3.84 MeV.
- C_log runs from −1.04 to +1.19. All R → 1 at q → 1.
- `q⁶ − 1 | R − 1` holds exactly for the k = 0 words, matching P2's factor.
- No word is selected.

### 2.4 P3 index character

- `log χ(p)/χ(n) = 2 ln q₀ = 0.208681`.
- `log χ(e⁻) = 3 ln q₀ = 0.313022`.
- Balance `Q/κ = −5 ln q₀ = −0.521704`. That needs κ = −1.4996 MeV, which contradicts
  `E(e⁻) > 0` (§1.4).

## 3. Derived vs posited

| item | status |
|---|---|
| log-additivity on one-strand joins; cross term = log ratio; ν̄ ↦ 0 | **proved** (Lean, sorry-free) |
| additivity on disjoint blocks | conditional on `TowerSpan` (unproved) |
| dropping `[N]_q!/q^N` | **required** for additivity (log of the factor is not additive: 4.22 at 3+2+1); a choice of the route, stated |
| κ magnitude | **not derived**; corpus offers α = E₀ (named) |
| κ sign | corpus convention +; the P2 words need − for both orderings |
| P3 sign problem | survives (Lean) |
| nucleon words (nuc11), lepton linking letters | corpus words / chosen letters, as in P2 |

## 4. What remains open

**Derivation of κ.** κ needs both a magnitude and a sign, together with a reason that `log|tr|`
is an energy at all. The free-energy reading cannot supply that reason (`FreeEnergySigned`).
Additivity cannot select κ, by construction.

**The owner's choice, if the route continues.** These are not enacted.

1. **Adopt κ = +E₀ (the corpus binding sign).**
   - What it means: keep one sign across binding and decay.
   - Result: on the P2 words, Q_β < 0 (β⁻ forbidden) and the electron has negative energy.
   - Risk: none to the corpus; nothing changes.
2. **Adopt κ = −E₀ for the mass/decay channel.**
   - What it means: the decay channel and the binding channel get opposite signs.
   - Result: Q = +0.489 MeV (−37.5 %).
   - It needs a reason that is not this number. Without one, it is a sign selected against the
     target.
3. **Stop route L as an energy theory.** Keep the Lean as the record that the log-trace is
   additive and that the scale is undetermined. Return to a derived nucleon/lepton word (the
   γγ/SDP selection) first.

**Default:** nothing changes. My judgement is 3: neither sign is derived, and option 2 is
exactly the selection the NO-FITTING rule forbids.
