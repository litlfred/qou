//! H_9(q) computation of ³H β-decay at quark level.
//!
//! 9 strands: 3 quarks × 3 nucleons
//! Proton (0): strands 0,1,2 = u,u,d
//! Neutron(1): strands 3,4,5 = u,d,d  ← converting
//! Neutron(2): strands 6,7,8 = u,d,d
//!
//! β-decay: insert T_{3,5} = (σ₄σ₅)⁵ at strands 4,5
//! then Gröbner reduce the combined braid.

use std::collections::HashMap;

fn main() {
    let q: f64 = 1.10998;
    let ha = q - 1.0/q;
    let s = q.sqrt() - 1.0/q.sqrt();
    let z = 1.0 / (q.sqrt() + 1.0/q.sqrt());
    
    println!("H_9(q) β-DECAY OF ³H AT QUARK LEVEL");
    println!("q = {:.5}, HA = {:.6}, s = {:.6}, z = {:.6}", q, ha, s, z);
    println!();
    
    // For now: compute the T_{3,5} NF in H_3(q) at generators σ₄,σ₅
    // This is (σ₄σ₅)⁵ which uses generators 4 and 5 of the 9-strand braid.
    // In H_9: σ₄ and σ₅ are adjacent generators (|4-5|=1) so they have
    // the same Hecke and YB relations as σ₁,σ₂ in H_3.
    
    // The key question: what is the NUCLEAR braid word for ³H in H_9?
    // 
    // Each nucleon is a Borromean link:
    //   B_3(u,u,d) = (σ₁σ₂⁻¹)³  for proton (strands 0,1,2)
    //   B_3(u,d,d) = (σ₄σ₅⁻¹)³  for neutron 1 (strands 3,4,5)
    //   B_3(u,d,d) = (σ₇σ₈⁻¹)³  for neutron 2 (strands 6,7,8)
    //
    // But σ⁻¹ is NOT in H_9(q). In the Hecke algebra:
    //   σ⁻¹ = σ - (q - q⁻¹) = σ - HA
    //   (from σ² = HA·σ + 1 → σ(σ-HA) = 1 → σ⁻¹ = σ-HA)
    //
    // So σ₂⁻¹ = σ₂ - HA in H_9.
    //
    // Inter-nucleon crossings: Hopf links between nucleon pairs.
    // These crossings involve generators σ₂ (between strands 2,3)
    // and σ₅ (between strands 5,6).
    //
    // The FULL nuclear braid for ³H:
    //   β(³H) = [B_3 at (0,1,2)] × [Hopf at (2,3)] × [B_3 at (3,4,5)]
    //           × [Hopf at (5,6)] × [B_3 at (6,7,8)]
    
    println!("NUCLEAR BRAID FOR ³H:");
    println!("  Proton (0,1,2):  (σ₁(σ₂-HA))³ = Borromean");
    println!("  Hopf (2,3):      σ₂ (inter-nucleon crossing)");
    println!("  Neutron1 (3,4,5): (σ₄(σ₅-HA))³ = Borromean");
    println!("  Hopf (5,6):      σ₅ (inter-nucleon crossing)");
    println!("  Neutron2 (6,7,8): (σ₇(σ₈-HA))³ = Borromean");
    println!();
    
    println!("β-DECAY INSERTION:");
    println!("  T_{{3,5}} = (σ₄σ₅)⁵ inserted at converting neutron");
    println!("  This acts on strands 4,5 (the dd crossing of neutron 1)");
    println!();
    
    println!("AFTER INSERTION:");
    println!("  β(³H) × (σ₄σ₅)⁵");
    println!("  → Gröbner reduce in H_9(q)");
    println!("  → daughter NF + T_{{2,3}} (electron) + K_{{0,1}} (neutrino)");
    println!();
    
    println!("This is the computation that determines Q exactly.");
    println!("H_9 has up to 9! = 362880 words in the full symmetric group.");
    println!("The nuclear braid is a SPECIFIC word — its NF is much smaller.");
    println!();
    println!("Need: implement H_9(q) Gröbner reduction in the hecke-engine.");
    println!("The engine already handles H_A(q) for any A — just need A=9");
    println!("with the QUARK-LEVEL crossing coefficients instead of nuclear.");
}
