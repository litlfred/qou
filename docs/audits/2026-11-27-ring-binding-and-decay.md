# Binding and β decay on the ring-valued mass

**Date** 2026-11-27 · **Owner question** "Is there ring binding. And. Alpha/beta decay?" · **Bean** `qou-brng` (C2, epic `qou-myts`)
**Builds on** PR #9789 (ring mass `m = [2]ⁿ q^{−2w} tr_D`, electron `m_e = [4]/q³`, energy reading `U = −q∂_q log m`), PRs #9622 / #9786 (bond words)
**Probe** [`computations/probes/ring_binding/ring_binding_probe.py`](../../computations/probes/ring_binding/ring_binding_probe.py): every trace is an exact Laurent polynomial in `Z[q, q⁻¹]`, evaluated at the proton `q₀` only at the end (mpmath 50 dps). 7/7 checks.
**Scope** Measured values (m_e, AME, CODATA) appear only in comparison columns. Nothing is fitted or wired.

## 1. Result

1. **Log reading: the ring changes nothing for γγ bonds.** Each vertex `V(s) = σ_s σ_{s+1}⁻¹` has writhe 0. So free and bound words have the same writhe and the same strand count. The framing factor `[2]ⁿ q^{−2w}` then cancels exactly in `m_free / m_atom`. Every log-reading binding already reported (PRs #9587, #9622, #9659, #9786) is therefore already a ring binding. The ring matters for the electron (`w = 3`), not for these bonds. Check K1.
2. **Energy reading `B_U = U_free − U_atom = q∂_q log(m_atom/m_free)`: new numbers, all small, and exactly zero at `q = 1`.**
   - The value at `q = 1` vanishes for every word measured.
   - Every pairwise linking number of these closures is 0, so this is consistent with the #9789 candidate `U(1) = 3·lk` (Murakami's `V′(1) = −3·lk·V(1)`). That identity is still not formalised, so the zero is a measurement, not a theorem.
   - The energy-reading binding is therefore entirely a deformation effect.
3. **β decay in the energy reading is forbidden.**
   - #9789 gives `U_n − U_p = +2` exactly, so `Δ_np = (2/U_e)·m_e = 0.41133 MeV`.
   - That is less than `m_e`, so `Q_β = Δ_np − m_e = −0.09967 MeV`: the neutron is stable in this reading (CODATA `+0.78233` MeV).
   - On the raw-trace reading the neutron sits below the proton, so `Q_β < 0` there too.
   - A sibling result (PR #9767) proves that in either chart n−p and Δ−N come out with opposite signs, whatever the electron reading. So no electron reading fixes both.
4. **α decay is not computable yet.**
   - `Q_α` needs the binding of a parent above A = 4. The lightest α emitter is ⁸Be, which is 24 strands, and no bond rule is derived for it (PR #9622).
   - Only the A = 4 daughter (⁴He) exists, as a single passing class at length ≤ 4 (§2).

## 2. Numbers at q₀ (energy unit `m_e/U_e`, `U_e = 2.484628135`; tower `E₀ = 4.227483356` MeV)

| case | `−ln r` | `B_log` (MeV) | `B_U` (U units) | `B_U` at `q = 1` | `B_U` (MeV) | AME (comparison) |
|---|---|---|---|---|---|---|
| ²H `V2V3` (cheapest merging) | 1.378094837 | 5.825873 | +0.4038236 | 0 | +0.083052 | 2.224566 |
| ²H `V2V2V2` (junction only) | 0.001503970 | 0.006358 | −0.0593076 | 0 | −0.012197 | 2.224566 |
| ²H `V2` (one vertex) | 1.412909121 | 5.973050 | −0.6903039 | 0 | −0.141971 | 2.224566 |
| ³H `V2V3V4` | 1.397161650 | 5.906478 | −0.2079274 | 0 | −0.042763 | 8.481796 |
| ⁴He `V2V3V4V8` | A4 | A4 | A4 | A4 | A4 | 28.295674 |

The log column equals the raw-trace numbers already on record, as point 1 predicts. In the energy reading three of four words come out unbound, and the bound one gives 0.083 MeV against 2.22 MeV. This is a scope-(a) negative: these words, read this way, do not bind. It does not exclude the energy reading from a closure.

## 3. What this leaves open

- **Which reading is the binding?** The log reading (`E₀·ln`) and the energy reading (`−q∂_q ln`, the #9789 electron unit) differ by a whole derivative. Neither is derived as *the* binding functional, and the unify-the-scales thread (PR #9767) is working on the orientation. No choice is made here.
- **Bond selection** stays open (owner, 2026-11-27: "keep open").
- **α decay** waits on a derived bond rule that reaches A ≥ 8.
