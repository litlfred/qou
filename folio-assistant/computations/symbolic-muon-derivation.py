#!/usr/bin/env python3
"""
Symbolic derivation of m_μ/m_e from γγ pair production.

Everything in q. Integer LP dual checked at each step.
The muon is the SECOND generation lepton = cinquefoil T_{2,5}.

The question: does the same construction that gives the proton
(B₃ confinement + quark crossings + LP-derived gluon) also
determine the muon mass when applied to T_{2,5} instead of T_{2,3}?

Chain:
  γγ → T_{2,3} selects e⁻/e⁺ (generation 1)
  γγ → T_{2,5} selects μ⁻/μ⁺ (generation 2)
  The operator selection (Frobenius dual) determines which
  generation is produced. The mass comes from the tower.
"""

import sympy as sp

q = sp.Symbol('q', positive=True)
h = q - 1/q  # HA

NAMES = ['γ', 'σ₀', 'σ₁', 'L₊', 'L₋', 'e⁻']

def mul(nf, c, d, gen):
    """Multiply NF by (c·σ_gen + d·I) in H₃(q). Symbolic."""
    r = [sp.S(0)] * 6
    hq = q - 1/q
    if gen == 0:
        rules = [(0,[(1,c),(0,d)]), (1,[(1,c*hq),(0,c),(1,d)]), (2,[(3,c),(2,d)]),
                 (3,[(3,c*hq),(2,c),(3,d)]), (4,[(5,c),(4,d)]), (5,[(5,c*hq),(4,c),(5,d)])]
    else:
        rules = [(0,[(2,c),(0,d)]), (1,[(4,c),(1,d)]), (2,[(2,c*hq),(0,c),(2,d)]),
                 (3,[(5,c),(3,d)]), (4,[(4,c*hq),(1,c),(4,d)]), (5,[(5,c*hq),(3,c),(5,d)])]
    for src, targets in rules:
        if nf[src] == 0: continue
        for tgt, coeff in targets:
            r[tgt] += nf[src] * coeff
    return [sp.expand(x) for x in r]

def show(label, nf, q0=None):
    print(f"\n  {label}:")
    for i, v in enumerate(nf):
        s = sp.factor(v)
        if s != 0:
            print(f"    {NAMES[i]}: {s}")
            if q0:
                print(f"           = {float(s.subs(q, q0)):.6f}")
    net = sp.factor(sum(nf))
    print(f"    net = {net}")
    if q0:
        print(f"        = {float(net.subs(q, q0)):.6f}")

def trM(nf):
    """Markov trace (symbolic)."""
    zs = 1 / (sp.sqrt(q) + 1/sp.sqrt(q))
    return sum(nf[i] * [1, zs, zs, zs**2, zs**2, zs**3][i] for i in range(6))

def is_stable_at(nf, q0_val):
    """Check LP stability numerically at q0_val.
    (Gx)_γ = tr_M(x) ≥ 0 is the binding constraint."""
    import numpy as np
    z_val = 1.0 / (q0_val**0.5 + q0_val**(-0.5))
    h_val = q0_val - 1.0/q0_val

    # Gram matrix (corrected, tr_M(e⁻) = z³)
    G = np.array([
        [1, z_val, z_val, z_val**2, z_val**2, z_val**3],
        [z_val, h_val*z_val+1, z_val**2, h_val*z_val**2+z_val, z_val**3, h_val*z_val**3+z_val**2],
        [z_val, z_val**2, h_val*z_val+1, z_val**3, h_val*z_val**2+z_val, h_val*z_val**3+z_val**2],
        [z_val**2, z_val**3, h_val*z_val**2+z_val, h_val*z_val**3+z_val**2, h_val*(h_val*z_val**2+z_val)+z_val**2, h_val*(h_val*z_val**3+z_val**2)+h_val*z_val**2+z_val],
        [z_val**2, h_val*z_val**2+z_val, z_val**3, h_val*(h_val*z_val**2+z_val)+z_val**2, h_val*z_val**3+z_val**2, h_val*(h_val*z_val**3+z_val**2)+h_val*z_val**2+z_val],
        [z_val**3, h_val*z_val**3+z_val**2, h_val*z_val**3+z_val**2, h_val*(h_val*z_val**3+z_val**2)+h_val*z_val**2+z_val, h_val*(h_val*z_val**3+z_val**2)+h_val*z_val**2+z_val, h_val*(h_val*(h_val*z_val**3+z_val**2)+h_val*z_val**2+z_val)+h_val*z_val**3+z_val**2],
    ])

    vals = [float(v.subs(q, q0_val)) for v in nf]
    x = np.array(vals)
    Gx = G @ x
    return all(Gx >= -1e-10), Gx

q0 = 1.1099785955541805

print("MUON FROM γγ: FULL SYMBOLIC DERIVATION")
print("=" * 65)

# ══════════════════════════════════════════════════════════════
# STEP 1: γγ pair production
# ══════════════════════════════════════════════════════════════
print("\n━━━ STEP 1: γγ PAIR PRODUCTION ━━━")
print("  γ = 𝟙 (identity in H₃(q))")
print("  T_{2,3} (trefoil) → e⁻/e⁺ (generation 1)")
print("  T_{2,5} (cinquefoil) → μ⁻/μ⁺ (generation 2)")

# ══════════════════════════════════════════════════════════════
# STEP 2: Electron = T_{2,3} = σ₀σ₁σ₀
# ══════════════════════════════════════════════════════════════
print("\n━━━ STEP 2: ELECTRON = T_{2,3} ━━━")
e = [sp.S(0)]*6; e[5] = sp.S(1)  # e⁻ = σ₀σ₁σ₀
show("e⁻ (trefoil)", e, q0)

stable_e, Gx_e = is_stable_at(e, q0)
print(f"\n  LP stable: {'YES ✓' if stable_e else 'NO ✗'}")

# ══════════════════════════════════════════════════════════════
# STEP 3: Muon = T_{2,5} = σ₀σ₁σ₀σ₁σ₀
# ══════════════════════════════════════════════════════════════
print("\n━━━ STEP 3: MUON = T_{2,5} = σ₀σ₁σ₀σ₁σ₀ ━━━")

# Build T_{2,5} step by step, checking LP at each intermediate
mu = [sp.S(1)] + [sp.S(0)]*5  # start with identity

steps = [
    ("σ₀ (#1)", 1, 0, 0),
    ("σ₁ (#2)", 1, 0, 1),
    ("σ₀ (#3)", 1, 0, 0),
    ("σ₁ (#4)", 1, 0, 1),
    ("σ₀ (#5)", 1, 0, 0),
]

for i, (name, c, d, gen) in enumerate(steps):
    mu = mul(mu, c, d, gen)
    stable, Gx = is_stable_at(mu, q0)
    net_val = float(sum(v.subs(q, q0) for v in mu))
    trM_val = float(sp.nsimplify(trM(mu)).subs(q, q0))

    neg_channels = []
    for j in range(6):
        if Gx[j] < -1e-10:
            neg_channels.append(f"{NAMES[j]}={Gx[j]:.4f}")

    status = "✓" if stable else f"✗ ({', '.join(neg_channels)})"
    print(f"  [{i+1}] {name:12s} net={net_val:+.4f}  tr_M={trM_val:+.6f}  LP {status}")

    if not stable:
        print(f"      → UNSTABLE! Need gluon before next step.")
        print(f"      Trying integer LP stabilizers...")

        # Try each stabilizer
        stabilizers = [
            ("σ₀",  lambda nf: mul(nf, 1, 0, 0)),
            ("σ₁",  lambda nf: mul(nf, 1, 0, 1)),
            ("σ₀⁻¹", lambda nf: mul(nf, 1, -(q-1/q), 0)),
            ("σ₁⁻¹", lambda nf: mul(nf, 1, -(q-1/q), 1)),
            ("L₊",  lambda nf: mul(mul(nf, 1, 0, 0), 1, 0, 1)),
            ("L₋",  lambda nf: mul(mul(nf, 1, 0, 1), 1, 0, 0)),
        ]

        best = None
        for sname, sfunc in stabilizers:
            nf_s = sfunc(mu)
            stable_s, Gx_s = is_stable_at(nf_s, q0)
            if stable_s:
                trM_s = float(sp.nsimplify(trM(nf_s)).subs(q, q0))
                if best is None or abs(trM_s) < abs(best[2]):
                    best = (sname, nf_s, trM_s)

        if best:
            print(f"      LP selects: {best[0]} (|tr_M| = {abs(best[2]):.6f})")
            mu = best[1]
            stable2, _ = is_stable_at(mu, q0)
            print(f"      After gluon: stable={stable2}")
        else:
            # Try double stabilizers
            print(f"      No single stabilizer works, trying double...")
            for s1name, s1func in stabilizers:
                nf_s1 = s1func(mu)
                stable_s1, _ = is_stable_at(nf_s1, q0)
                if not stable_s1: continue
                for s2name, s2func in stabilizers:
                    nf_s2 = s2func(nf_s1)
                    stable_s2, _ = is_stable_at(nf_s2, q0)
                    if stable_s2:
                        trM_s2 = float(sp.nsimplify(trM(nf_s2)).subs(q, q0))
                        if best is None or abs(trM_s2) < abs(best[2]):
                            best = (f"{s1name}→{s2name}", nf_s2, trM_s2)

            if best:
                print(f"      LP selects: {best[0]} (|tr_M| = {abs(best[2]):.6f})")
                mu = best[1]

muon_nf = [sp.factor(x) for x in mu]
show("Muon (final, with any gluon)", muon_nf, q0)

stable_mu, Gx_mu = is_stable_at(muon_nf, q0)
print(f"\n  Final LP stable: {'YES ✓' if stable_mu else 'NO ✗'}")

# ══════════════════════════════════════════════════════════════
# STEP 4: Mass ratio
# ══════════════════════════════════════════════════════════════
print("\n━━━ STEP 4: MASS RATIO ━━━")

# Per-generator vertex volumes (symbolic)
def vol_sym(crossings):
    a, b = sp.S(0), sp.S(1)
    sp_v, ap = sp.S(1), sp.S(1)
    hq = q - 1/q
    zs = 1/(sp.sqrt(q) + 1/sp.sqrt(q))

    # Wedderburn weights (symbolic)
    def qint(k): return (q**k - q**(-k)) / (q - q**(-1))
    nf3 = qint(1)*qint(2)*qint(3)
    ws = sp.S(1)**2 / nf3  # dim(sym)=1
    wa = sp.S(1)**2 / nf3  # dim(alt)=1
    wd = qint(3)**2 / nf3  # dim(std)=[3]_q
    wt = ws + wd + wa
    ws /= wt; wd /= wt; wa /= wt

    for c, d in crossings:
        a, b = sp.expand(a*c*hq + a*d + b*c), sp.expand(a*c + b*d)
        sp_v = sp.expand(sp_v * (c*q + d))
        ap = sp.expand(ap * (-c/q + d))
    Vs = sp.expand(zs*a + b)
    return sp.expand(ws*sp_v + wd*Vs + wa*ap)

# Count how many crossings the muon ended up with
# The T_{2,5} braid word is σ₀σ₁σ₀σ₁σ₀
# On 3 strands: gen 0 gets crossings at positions 1,3,5 (3 crossings)
#                gen 1 gets crossings at positions 2,4 (2 crossings)
# Plus any gluon crossings added

# For the MASS TOWER, we need per-generator vertex volumes
# Electron (T_{2,3} on 2 strands): 1 gen, 3 crossings
Ve_sym = vol_sym([(1, 0)] * 3)

# Muon (T_{2,5} on 2 strands): 1 gen, 5 crossings
Vmu_2strand = vol_sym([(1, 0)] * 5)

# Muon (T_{2,5} on 3 strands): 2 gens, split 3+2
Vmu_g0 = vol_sym([(1, 0)] * 3)  # gen 0: σ₀ at positions 1,3,5
Vmu_g1 = vol_sym([(1, 0)] * 2)  # gen 1: σ₁ at positions 2,4

print("  Vertex volumes (symbolic):")
print(f"    V̂_e (2-strand, 3 cross) = {sp.simplify(Ve_sym)}")
print(f"    V̂_e at q₀ = {float(Ve_sym.subs(q, q0)):.6f}")
print()
print(f"    V̂_μ (2-strand, 5 cross) = {sp.simplify(Vmu_2strand)}")
print(f"    V̂_μ at q₀ = {float(Vmu_2strand.subs(q, q0)):.6f}")
print()
print(f"    V̂_μ₀ (3-strand gen 0, 3 cross) = {sp.simplify(Vmu_g0)}")
print(f"    V̂_μ₁ (3-strand gen 1, 2 cross) = {sp.simplify(Vmu_g1)}")
print(f"    at q₀: V̂₀ = {float(Vmu_g0.subs(q, q0)):.6f}, V̂₁ = {float(Vmu_g1.subs(q, q0)):.6f}")

# Mass tower (numeric at q₀ for Φ_q)
qi0 = 1.0/q0
z0 = 1.0/(q0**0.5 + qi0**0.5)

def Phi_q_num(x):
    if abs(x) >= q0: return float('inf')
    p = 1.0
    for k in range(1, 2001):
        f = 1.0 - qi0**k * x
        if abs(f) < 1e-300: return float('inf')
        p /= f
        if abs(qi0**k * x) < 1e-15: break
    return p

def mass_num(vols):
    desc = 1.0
    for v in vols: desc *= v
    desc = abs(desc)
    single = sum(Phi_q_num(abs(v)) for v in vols)
    cross = sum(z0**2 * Phi_q_num(abs(vols[i]*vols[i+1])) for i in range(len(vols)-1))
    return desc + single + cross

Ve_num = float(Ve_sym.subs(q, q0))
Vmu_2s_num = float(Vmu_2strand.subs(q, q0))
Vmu_g0_num = float(Vmu_g0.subs(q, q0))
Vmu_g1_num = float(Vmu_g1.subs(q, q0))

me = mass_num([Ve_num])
mmu_2s = mass_num([Vmu_2s_num]) if abs(Vmu_2s_num) < q0 else float('inf')
mmu_3s = mass_num([Vmu_g0_num, Vmu_g1_num]) if abs(Vmu_g0_num) < q0 and abs(Vmu_g1_num) < q0 else float('inf')

print()
print("━━━ MASS TOWER RESULTS ━━━")
print(f"  Electron (2-strand): 𝔪_e = {me:.2f}")
print(f"  Muon (2-strand, 5 cross): 𝔪_μ = {mmu_2s:.2f}")
if mmu_2s < float('inf'):
    print(f"    m_μ/m_e = {mmu_2s/me:.4f}  (CODATA: 206.7683)")
print(f"  Muon (3-strand, 3+2 cross): 𝔪_μ = {mmu_3s:.2f}")
if mmu_3s < float('inf'):
    print(f"    m_μ/m_e = {mmu_3s/me:.4f}  (CODATA: 206.7683)")

# ══════════════════════════════════════════════════════════════
# STEP 5: Does the muon need gluon like the proton?
# ══════════════════════════════════════════════════════════════
print()
print("━━━ STEP 5: DOES THE MUON NEED GLUON? ━━━")
print("  The proton needed 2×σ₀ gluon because the 9-cross")
print("  element was LP unstable at q₀.")
print()
print("  The muon T_{2,5} construction:")

# Check NF LP stability at each step of T_{2,5}
mu_test = [sp.S(1)] + [sp.S(0)]*5
print(f"  Step-by-step LP check:")
for i, (name, c, d, gen) in enumerate(steps):
    mu_test = mul(mu_test, c, d, gen)
    stable, Gx = is_stable_at(mu_test, q0)
    trM_val = sum(float(v.subs(q, q0)) * w for v, w in
                  zip(mu_test, [1, z0, z0, z0**2, z0**2, z0**3]))
    print(f"    [{i+1}] {name}: tr_M={trM_val:+.6f}, LP {'✓' if stable else '✗'}")

# The muon on 2 strands is σ₀⁵: just 5 crossings on 1 gen
# Its NF in H₂(q) is trivial — it's just the accumulated product
# On 2 strands there's no Frobenius constraint to violate
# (H₂(q) has basis {1, σ₀}, Gram is 2×2, always positive for q > 1)
print()
print("  On 2 STRANDS: H₂(q) has basis {γ, σ₀}")
print("  The Gram matrix is 2×2, always positive definite for q > 1")
print("  → Muon on 2 strands is ALWAYS LP stable. No gluon needed.")
print("  → The muon mass is PURELY determined by V̂ = vol(5 crossings)")
print(f"  → V̂_μ = {float(Vmu_2strand.subs(q, q0)):.6f}")
print(f"  → m_μ/m_e = {mmu_2s/me:.4f} (CODATA: 206.77)")
print()
print("  The gap: 48.3 vs 206.8 (factor 4.3)")
print("  Missing physics: the muon may involve INTERNAL structure")
print("  (like the proton's B₃ + quarks) that we haven't modelled.")
