"""⁴He (A=4) end-to-end validation of the recursion-kernel A-operator.

Confirms that the operator-valued Wenzl combiner (`a_operator_recursive`) — which
peels the last nucleon (an H_3 block) off the canonical ⁴He atom word and builds
`A^λ_{ξν}(I)` in the Young/GT basis without the `d_λ` ambient — reproduces the
production binding observable at A=4:

  (a) per-λ combiner χ^λ vs direct `young_seminormal.chi_young` on the *same*
      ⁴He word (identical constant promotion) — airtight, ~2e-47 ≪ 1e-25;
  (b) end-to-end `tr_M(⁴He) = Σ_λ y_λ χ^λ` vs the canonical fine-Bratteli
      transfer matrix (`tr_m_atom_via_transfer`) — relative ~2e-16, at the
      float64 floor of the atom word's stored crossing constants (the
      transfer re-lifts the float word; the per-λ-vs-transfer gap of ~6e-15 is
      that convention floor, not a kernel error — (a) shows the kernel is exact).

Honest framing (no production-value change): per the main-merged bond-dimension
verdict `χ_eff(k)=p(3k)`, the combiner cannot beat the transfer asymptotically;
this validates it as an independent A≥4 cross-check, not a replacement. The ρ_ξ
build here is a direct d_ξ≤216 mpmath evaluation (~24 min); a production wiring
would compute ρ_ξ recursively.

Run: `python3 a_operator_recursive_he4_crosscheck.py` (~25 min at 50 dps).
"""
import time, mpmath as mp
mp.mp.dps = 60
import a_operator_categorical as aoa
import a_operator_recursive as rec
from young_seminormal import chi_young, standard_tableaux
from mass_at_3A_proper import atom_braid_word_3A
from reduced_block_kernel import chi_all_lambda_reduced_block
from wedderburn_jones_markov import y_lambda_at
from q_parameter import Q as Q0
from lr_coefficients import partitions_of

dps = 50
q = aoa.q0_mp(dps); q_str = mp.nstr(q, dps)
w = atom_braid_word_3A(2, 2)
idx = next(i for i, (c, d, g) in enumerate(w) if g == 8)
W_inner = w[:idx]; I_c, I_d, I_g = w[idx]; assert I_g == 8
block = [(c, d, g - 9) for (c, d, g) in w[idx + 1:]]
print(f"4He: W_inner={len(W_inner)} bridge d={mp.nstr(I_d,6)} block={len(block)}", flush=True)

def prod(mats, word):
    M = mp.eye(mats[0].rows)
    for (c, d, g) in word:
        M = M * (mp.mpf(c) * mats[g] + mp.mpf(d) * mp.eye(mats[0].rows))
    return M

p9, p3 = partitions_of(9), partitions_of(3)
t0 = time.time()
RW = {xi: prod(aoa.exact_seminormal_matrices(xi, q_str, dps)[0], W_inner) for xi in p9}
RB = {nu: prod(aoa.exact_seminormal_matrices(nu, q_str, dps)[0], block) for nu in p3}
print(f"rho builds: {time.time()-t0:.1f}s", flush=True)

def trace_A_kron(A, RWx, RBn, d_mu, d_nu):
    # Tr[A . kron(RWx,RBn)] = sum_{a,b,a',b'} A[a*d_nu+b, a'*d_nu+b'] RWx[a',a] RBn[b',b]
    s = mp.mpf(0)
    for a in range(d_mu):
        for ap in range(d_mu):
            rwa = RWx[ap, a]
            if rwa == 0: continue
            for b in range(d_nu):
                for bp in range(d_nu):
                    rbb = RBn[bp, b]
                    if rbb == 0: continue
                    s += A[a*d_nu+b, ap*d_nu+bp] * rwa * rbb
    return s

t0 = time.time(); chi_comb = {}
for lam in partitions_of(12):
    A = rec.interface_blocks(lam, 9, 3, q_str, mp.mpf(I_d), dps)
    s = mp.mpf(0)
    for (xi, nu), info in A.items():
        s += trace_A_kron(info["A"], RW[xi], RB[nu], info["d_mu"], info["d_nu"])
    chi_comb[lam] = s
print(f"combiner all-77 chi: {time.time()-t0:.1f}s", flush=True)

print("=== (a) combiner vs direct chi_young (real 4He word, d<=120) ===", flush=True)
worst = mp.mpf(0); n_ok = 0
for lam in partitions_of(12):
    if len(standard_tableaux(lam)) > 120: continue
    ad = abs(chi_comb[lam] - chi_young(lam, w, q)); worst = max(worst, ad); n_ok += 1
print(f"  {n_ok} lambda: max|chi_comb-chi_young| = {mp.nstr(worst,6)}", flush=True)

print("=== (b) end-to-end tr_M(4He): combiner vs transfer ===", flush=True)
y = {tuple(k): mp.mpf(str(v)) for k, v in y_lambda_at(12, Q0).items()}
chi_ref = chi_all_lambda_reduced_block(w, 12, q=None)
chi_ref = {tuple(k): (v if isinstance(v, mp.mpf) else mp.mpf(str(v))) for k, v in chi_ref.items()}
worst_ref = max(abs(chi_comb[k] - chi_ref[k]) for k in chi_comb)
trM_comb = sum((y[k]*chi_comb[k] for k in chi_comb), mp.mpf(0))
trM_ref  = sum((y[k]*chi_ref[k]  for k in chi_ref),  mp.mpf(0))
print(f"  per-lambda max|chi_comb-chi_transfer| (all 77) = {mp.nstr(worst_ref,6)}", flush=True)
print(f"  tr_M_combiner = {mp.nstr(trM_comb,18)}", flush=True)
print(f"  tr_M_transfer = {mp.nstr(trM_ref,18)}", flush=True)
print(f"  |dtr_M|={mp.nstr(abs(trM_comb-trM_ref),6)}  rel={mp.nstr(abs(trM_comb-trM_ref)/abs(trM_ref),6)}", flush=True)
