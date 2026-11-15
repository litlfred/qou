#!/usr/bin/env python3
"""Write ms_plan.json — the pre-registered list of starts (see preregistration.md)."""
import json
import ms_words as W
R1 = "../curves/"
BEST = {"nuc9": R1 + "nuc9_N256_ext.npz", "A": R1 + "gluon_s1_s0_N256.npz",
        "B": R1 + "gluon_s0_s1_N256_ext.npz", "G": R1 + "nuc11_gen_grouped_N128.npz",
        "hopf": R1 + "cal_hopf_s1^2_N256_ext.npz"}
BR = [(64, 6000, 1e-6), (128, 4000, 1e-6), (256, 3000, 1e-8)]
CU = [(128, 4000, 1e-6), (256, 3000, 1e-8)]
names = {
    "nuc9": dict(canon="nuc9", partner="nuc9_rot4", rot=("nuc9", 7), dconj="nuc9_dconj", rew="nuc9_rewrite",
                 st="nuc9_stabtop", sb="nuc9_stabbot"),
    "A": dict(canon="gluon_s1_s0", partner="gluon_s1_s1", rot=("gluon_s1_s0", 5), dconj="A_dconj", rew="A_rewrite",
              st="A_stabtop", sb="A_stabbot"),
    "B": dict(canon="gluon_s0_s1", partner="gluon_s0_s0", rot=("gluon_s0_s1", 5), dconj="B_dconj", rew="B_rewrite",
              st="B_stabtop", sb="B_stabbot"),
    "G": dict(canon="gen_grouped", partner="G_rot3", rot=("gen_grouped", 9), dconj="G_dconj", rew="G_rot9",
              st="G_stabtop", sb="G_stabbot"),
}
plan = []
def br(cls, i, word, R, zamp=1.0, warp_seed=None, warp_amp=0.6, word_list=None, strands=None, note=""):
    d = dict(id=f"{cls}_s{i:02d}", cls=cls, kind="braid", word=word, R_over_a=R, zamp=zamp,
             warp_seed=warp_seed, warp_amp=warp_amp, schedule=BR, note=note)
    if word_list is not None: d.update(word_list=word_list, strands=strands)
    plan.append(d)
for cls, nm in names.items():
    w0, n0 = W.REPS[cls][nm["canon"]]
    br(cls, 1, nm["canon"], 3.0, note="route-1 canonical start (reproduction)")
    br(cls, 2, nm["canon"], 2.0, zamp=1.5, warp_seed=101, note="R/a=2, tall crossings, warped slices")
    br(cls, 3, nm["canon"], 5.0, zamp=0.6, warp_seed=102, note="R/a=5, flat crossings, warped slices")  # float64-ok: numerical gradient flow of a discretised curve energy is float64 by design; results are stated as float64 upper bounds, never as identities
    br(cls, 4, nm["canon"], 3.5, zamp=1.0, warp_seed=103, warp_amp=0.85, note="R/a=3.5, strongly warped slices")  # float64-ok: numerical gradient flow of a discretised curve energy is float64 by design; results are stated as float64 upper bounds, never as identities
    br(cls, 5, nm["partner"], 3.0, note="conjugate word")
    rw, k = nm["rot"]; ww, nn = W.REPS[cls][rw]
    br(cls, 6, f"{rw}_rot{k}", 2.5, zamp=1.2, word_list=W.rot(ww, k), strands=nn, note="cyclic rotation")  # float64-ok: numerical gradient flow of a discretised curve energy is float64 by design; results are stated as float64 upper bounds, never as identities
    br(cls, 7, nm["dconj"], 3.0, note="Delta-conjugate (s0<->s1)")
    br(cls, 8, nm["rew"], 4.0, warp_seed=104, note="braid-relation rewrite / other rotation")
    br(cls, 9, nm["st"], 3.0, note="DIFFERENT braid rep: Markov stabilisation, 4 strands (top)")
    br(cls, 10, nm["sb"], 3.0, note="DIFFERENT braid rep: Markov stabilisation, 4 strands (bottom)")
    for i, s in ((11, 11), (12, 12)):
        plan.append(dict(id=f"{cls}_s{i:02d}", cls=cls, kind="mobius", source=BEST[cls], seed=s, schedule=CU,
                         note="random orientation-preserving Möbius image of route-1 best curve"))
    for i, (eps, s) in ((13, (0.05, 13)), (14, (0.15, 14))):
        plan.append(dict(id=f"{cls}_s{i:02d}", cls=cls, kind="perturb", source=BEST[cls], eps=eps, seed=s, schedule=CU,
                         note=f"random smooth perturbation eps={eps} of route-1 best curve"))
# calibration controls, same batch
for sid, word, R in (("hopf_c1", "hopf_s1^2", 3.0), ("hopf_c2", "hopf_3strand", 3.0),
                     ("trefoil_c1", "trefoil_s1^3", 3.0), ("trefoil_c2", "trefoil_3strand", 3.0)):
    plan.append(dict(id=sid, cls=sid.split("_")[0], kind="braid", word=word, R_over_a=R, zamp=1.0, warp_seed=None,
                     schedule=BR, note="calibration control"))
plan.append(dict(id="hopf_c3", cls="hopf", kind="mobius", source=BEST["hopf"], seed=31, schedule=CU,
                 note="calibration: Möbius image of route-1 Hopf"))
json.dump(plan, open("ms_plan.json", "w"), indent=1)
print(len(plan), "starts")
