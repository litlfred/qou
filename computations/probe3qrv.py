import _path_bridge, sympy as sp, mpmath as mp
from _precision import set_compute_dps  # noqa: E402
set_compute_dps()
from q_parameter import Q_MP as Q
from markov.markov_peel import word_to_element
from markov.markov_trace_canonical import tr_M_element
from hecke_symbolic import q as qsym, HA as H_SYMB, z_markov as Z_SYMB

q0 = sp.Float(str(Q), 50)
h0 = q0 - 1/q0
z0 = q0**3 / (q0**2 + 1)
print("q0 =", q0, " h0 =", sp.N(h0, 25), " z0 =", sp.N(z0, 25))


def trace_word(word, n=3, label=""):
    e = word_to_element(word)
    t = tr_M_element(e, n, z=Z_SYMB, h=H_SYMB, simplify=False)
    val = sp.N(t.subs({Z_SYMB: z0, H_SYMB: h0, qsym: q0}), 30)
    print("  %-42s -> %s" % (label, val))
    return val


hn = float(h0)
bor_interleaved = [(1.0, 0.0, 0), (1.0, -hn, 1)] * 3
bor_grouped = [(1.0, 0.0, 0)] * 3 + [(1.0, -hn, 1)] * 3

print("\n[1] Markov trace of the PURE Borromean word, same machinery:")
v_int = trace_word(bor_interleaved, 3, "(s0 s1^-1)^3 interleaved (true beta_Bor)")
v_grp = trace_word(bor_grouped, 3, "s0^3 s1^-3   grouped (atomic-word core)")

print("\n[2] Full atomic word (Z=1,N=0) = tr_M_atomic(1,0):")
from mass_at_3A_proper import atom_braid_word_3A
aw = atom_braid_word_3A(1, 0)
print("     len =", len(aw))
v_atom = trace_word(aw, 3, "atom_braid_word_3A(1,0) (11 letters)")

print("\n[3] Convention D closed form (production):")
hD = mp.mpf(str(Q)) - 1/mp.mpf(str(Q))
D = abs((4 + hD**2 - 3*hD**4 - hD**6)/(hD**2 + 4))
print("  D =", mp.nstr(D, 25))

print("\n[4] Ratios vs D:")
Dv = sp.Float(mp.nstr(D, 40), 40)
for name, v in [("interleaved beta_Bor", v_int),
                ("grouped s0^3s1^-3", v_grp),
                ("atomic 11-letter", v_atom)]:
    print("  |%-22s| / D = %s" % (name, sp.N(abs(v)/Dv, 20)))
