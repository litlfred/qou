# Hecke-channel (chirality) binding — `B_sym-ch` / `m_sym-ch` (2026-06-17)

**Probe:** [`computations/probes/hecke_channel_binding_probe.py`](../../computations/probes/hecke_channel_binding_probe.py)
· witness `computations/hecke-channel-binding.witness.json`
**Trigger:** owner question — *"there are no chirality-negative
inter-nucleon crossings anywhere in the canonical construction… maybe
the constraint needs modification to pick up chirality?"*

## The physical red flag (owner's point, confirmed)

The canonical binding kernel uses ONE Wedderburn channel of each
inter-nucleon crossing — the **standard** channel `V_std = z·c + d` —
for every bond type. That construction has **no chirality**, and the
symptom is concrete: it **binds the unbound channels**. Experimentally
the **diproton (pp) and dineutron (nn) have no bound state**; only the
deuteron (pn, spin-triplet) binds. But `V_std` gives `f_pp = 0.499 →
+2.91 MeV` and `f_nn = 0.290 → +5.18 MeV` of binding. That is a genuine
defect: the kernel cannot tell bound from unbound because it ignores the
spin/isospin (Pauli) channel.

## The three Hecke channels per crossing

Each crossing `(c,d)` carries (substrate weights
`w_sym = w_alt = q²/(q⁴+4q²+1)`, `w_std = (q²+1)²/(q⁴+4q²+1)`):

| channel | value | role |
|---------|-------|------|
| symmetric `s` | `c·q + d` (eigenvalue `+q`) | triplet-like |
| standard `V_std` | `z·c + d` | the one the kernel currently uses |
| alternating `a` | `−c·q⁻¹ + d` (eigenvalue `−q⁻¹`) | singlet / Pauli |
| full | `w_sym·s + w_std·V_std + w_alt·a` | — |

At q₀ (bonds pp=(1,0), nn=(1,−h), pn=(1,−h/2), `h=q−q⁻¹`):

| bond | sym | std | alt | Vfull |
|------|-----|-----|-----|-------|
| pp | 1.110 | 0.499 | −0.901 | 0.369 |
| nn | 0.901 | 0.290 | −1.110 | 0.160 |
| pn | 1.005 | 0.395 | −1.005 | 0.264 |

## Partial positive finding

The **alternating (antisymmetric / Pauli) channel makes BOTH pp and nn
unbound** (`|f| ≥ 1` for nn; `f_pp<0` antibound) — exactly the
diproton/dineutron physics. So the chirality the owner expected **is in
the substrate**, in the alternating channel. The Pauli structure is real.

## `B_sym-ch` / `m_sym-ch` dashboard (per nucleus, complete graph)

`B_chan(K) = E₀·Σ_bonds [log(1/f_bond^chan) if bound else 0]`,
`E₀ ≈ 4.186 MeV`; `m_sym-ch = Z·m_p + N·m_n − B_sym-ch`.

| nuc | AME B | B_std | **B_sym-ch** | B_alt-ch | B_Vfull | **m_sym-ch** | m_meas |
|-----|------:|------:|-----:|-----:|------:|---------:|-------:|
| D   | 2.225 | 3.890 | **0.000** | 0.000 | 5.573 | 1877.838 | 1875.613 |
| T   | 8.482 | 12.96 | **0.437** | 0.000 | 18.83 | 2816.966 | 2808.921 |
| ³He | 7.718 | 10.69 | **0.000** | 0.437 | 15.32 | 2816.110 | 2808.392 |
| ⁴He | 28.30 | 23.65 | **0.437** | 0.000 | 34.15 | 3755.238 | 3727.379 |

## Verdict — the channel/chirality variant does **not** close binding

- **`B_sym-ch` ≈ 0** for every nucleus — the symmetric channel is too
  weak (`f^sym ≈ 1`); `m_sym-ch` overshoots the measured mass by ≈ the
  full binding. So `B_sym-ch` is not the binding mechanism.
- `B_std` (current) overbinds D/T/³He and underbinds ⁴He; `B_Vfull`
  overbinds further. **No single channel** gives the physical picture
  (pp,nn unbound **and** pn bound) simultaneously.
- **Deuteron crux persists.** AME requires `f_pn = 0.588`; the channels
  bracket it (`std = 0.395` overbinds, `sym = 1.005` unbinds) but no
  substrate-determined channel or weight lands on 0.588. Choosing a
  channel weight to hit 0.588 would be a fit (Δ_λ-gated, rejected).

**Net:** the owner is right that chirality is missing and that the
substrate carries it (alternating channel = Pauli, pp/nn correctly
unbound). But the Hecke channel structure alone does not close the
deuteron — the obstruction is the same fractional/specific pn coupling
(`f_pn = 0.588`) seen in every prior crossing-counting probe. This is a
real structural observation (the kernel SHOULD use the alt channel for
pp/nn to stop binding the unbound channels), not a binding closure.
Recorded as a tracked variant (`B_sym-ch`, `m_sym-ch`).
