import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
import sys; sys.path.insert(0,'.')
from mpmath import mp, mpf, fabs, catalan
from _precision import set_compute_dps  # noqa: E402
set_compute_dps()
from q_parameter import Q_50_DIGIT_STR
from tr_m_wenzl_bridge_mpfr import tr_M_via_wenzl_bridge_mpfr
from hecke_core import _PROTON_G0,_PROTON_G1,_NEUTRON_G0,_NEUTRON_G1, h as H
from codata_constants import M_E_MEV, AME_B_HE3_MEV_VALIDATION, AME_B_TRITIUM_MEV_VALIDATION
qs=Q_50_DIGIT_STR; q=mpf(qs); m_e=mpf(str(M_E_MEV)); VOL=8*catalan; h=float(H)

def block(nuc,k):
    g0=_PROTON_G0 if nuc=='p' else _NEUTRON_G0
    g1=_PROTON_G1 if nuc=='p' else _NEUTRON_G1
    return [(float(c),float(d),3*k) for c,d in g0]+[(float(c),float(d),3*k+1) for c,d in g1]

def cross(a,b):  # pp:(1,0) nn:(1,-h) pn:(1,-h(1/2-delta/4))
    if a=='p' and b=='p': return (1.0,0.0)
    if a=='n' and b=='n': return (1.0,-h)
    # colour-WEIGHTED p-n interface (qou-gdtb). Was -h/2, the
    # colour-blind value, which deletes the p/n asymmetry.
    from canonical_braid_crossings import _avg_color_delta
    return (1.0, -h * (0.5 - float(_avg_color_delta()) / 4))

def trM(word,n): return fabs(mpf(str(tr_M_via_wenzl_bridge_mpfr(word,n,qs,dps=50))))

# 3-nucleon all-pairs H9: blocks 0,1,2 ; bonds 0-1(gen2), 1-2(gen5),
# long-range 0-2 realized by conjugation σ3σ4σ5·(cross)·σ5σ4σ3 bringing
# block-2 head adjacent to block-0 tail.
def allpairs_word(order):
    o=order
    w=block(o[0],0)+block(o[1],1)+block(o[2],2)
    w+=[(*cross(o[0],o[1]),2)]              # bond 0-1
    w+=[(*cross(o[1],o[2]),5)]              # bond 1-2
    # long-range 0-2: carry strand block2->near block0 via gens 3,4,5 then cross at gen2-side
    carry=[(1.0,0.0,g) for g in (5,4,3)]
    w+= carry + [(*cross(o[0],o[2]),2)] + carry[::-1]
    return w

def chain_word(order, bonds):
    o=order; w=block(o[0],0)+block(o[1],1)+block(o[2],2)
    if 0 in bonds: w+=[(*cross(o[0],o[1]),2)]
    if 1 in bonds: w+=[(*cross(o[1],o[2]),5)]
    return w

for iso,order,ame in [('3He',['p','p','n'],AME_B_HE3_MEV_VALIDATION),('3H',['p','n','n'],AME_B_TRITIUM_MEV_VALIDATION)]:
    ame=mpf(str(ame))
    vac=trM(chain_word(order,set()),9)
    allp=trM(allpairs_word(order),9)
    dtr_allpairs_joint = vac-allp
    # 2-body all-pairs sum already known: recompute as 3 single-bond chain defects + long-range
    print(f'{iso}: vac={float(vac):.5f} allpairs_joint_tr={float(allp):.5f} Δtr(joint all-pairs)={float(dtr_allpairs_joint):.5f}')
    B=m_e*VOL*dtr_allpairs_joint
    print(f'   B(joint all-pairs H9) = {float(B):.3f} vs AME {float(ame):.3f} ({float((B-ame)/ame*100):+.1f}%)')
