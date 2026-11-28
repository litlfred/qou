//! Deterministic $Z = 0\ldots 118$ `T3` colour-valence bond graph and Hopf atomic-chart generator.
//!
//! Implements the 2026-11-27 ruled `T3` colour-valence bound (`QOU/MassTheory/NucleusBondValence.lean`):
//! - Each nucleon carries 3 colour strands (`Red`, `Green`, `Blue`), permitting at most one
//!   inter-nucleon $\gamma\gamma$ bond per colour channel (maximum vertex degree $\le 3$ and a
//!   proper 3-edge-colouring of the simple inter-nucleon bond graph).
//! - Maximum bond count on $A$ nucleons:
//!   $$M_{\mathrm{T3}}(A) = \begin{cases} 0 & (A \le 1), \\ 1 & (A = 2), \\ \min\!\bigl(\binom{A}{2},\, 3\lfloor A/2 \rfloor\bigr) & (A \ge 3), \end{cases}$$
//!   reproducing the complete graphs $K_2, K_3, K_4$ with $1, 3, 6$ bonds at $A = 2, 3, 4$, and
//!   connected Class-1 proper 3-edge-coloured graphs with $3\lfloor A/2 \rfloor$ bonds for all $A \ge 5$.

use std::collections::{BTreeSet, VecDeque};

use serde::{Deserialize, Serialize};

use crate::hadron::{
    borromean_baryon_word, electron_hopf_word, NucleonKind, QuarkFlavour,
};
use crate::photon::BraidWord;

/// IUPAC element symbols for atomic numbers `Z = 0..=118` (`Z = 0` is the bare neutron `"n"`).
pub const ELEMENT_SYMBOLS: [&str; 119] = [
    "n", "H", "He", "Li", "Be", "B", "C", "N", "O", "F", "Ne", "Na", "Mg", "Al", "Si", "P", "S",
    "Cl", "Ar", "K", "Ca", "Sc", "Ti", "V", "Cr", "Mn", "Fe", "Co", "Ni", "Cu", "Zn", "Ga", "Ge",
    "As", "Se", "Br", "Kr", "Rb", "Sr", "Y", "Zr", "Nb", "Mo", "Tc", "Ru", "Rh", "Pd", "Ag", "Cd",
    "In", "Sn", "Sb", "Te", "I", "Xe", "Cs", "Ba", "La", "Ce", "Pr", "Nd", "Pm", "Sm", "Eu", "Gd",
    "Tb", "Dy", "Ho", "Er", "Tm", "Yb", "Lu", "Hf", "Ta", "W", "Re", "Os", "Ir", "Pt", "Au", "Hg",
    "Tl", "Pb", "Bi", "Po", "At", "Rn", "Fr", "Ra", "Ac", "Th", "Pa", "U", "Np", "Pu", "Am", "Cm",
    "Bk", "Cf", "Es", "Fm", "Md", "No", "Lr", "Rf", "Db", "Sg", "Bh", "Hs", "Mt", "Ds", "Rg", "Cn",
    "Nh", "Fl", "Mc", "Lv", "Ts", "Og",
];

/// Canonical valley-of-stability / longest-lived mass numbers $A$ for `Z = 0..=118`,
/// providing a deterministic 119-element reference chart (`N = A - Z`).
pub const CANONICAL_MASS_NUMBERS: [usize; 119] = [
    1,   // Z=0:  1n
    1,   // Z=1:  1H
    4,   // Z=2:  4He
    7,   // Z=3:  7Li
    9,   // Z=4:  9Be
    11,  // Z=5:  11B
    12,  // Z=6:  12C
    14,  // Z=7:  14N
    16,  // Z=8:  16O
    19,  // Z=9:  19F
    20,  // Z=10: 20Ne
    23,  // Z=11: 23Na
    24,  // Z=12: 24Mg
    27,  // Z=13: 27Al
    28,  // Z=14: 28Si
    31,  // Z=15: 31P
    32,  // Z=16: 32S
    35,  // Z=17: 35Cl
    40,  // Z=18: 40Ar
    39,  // Z=19: 39K
    40,  // Z=20: 40Ca
    45,  // Z=21: 45Sc
    48,  // Z=22: 48Ti
    51,  // Z=23: 51V
    52,  // Z=24: 52Cr
    55,  // Z=25: 55Mn
    56,  // Z=26: 56Fe
    59,  // Z=27: 59Co
    58,  // Z=28: 58Ni
    63,  // Z=29: 63Cu
    64,  // Z=30: 64Zn
    69,  // Z=31: 69Ga
    74,  // Z=32: 74Ge
    75,  // Z=33: 75As
    80,  // Z=34: 80Se
    79,  // Z=35: 79Br
    84,  // Z=36: 84Kr
    85,  // Z=37: 85Rb
    88,  // Z=38: 88Sr
    89,  // Z=39: 89Y
    90,  // Z=40: 90Zr
    93,  // Z=41: 93Nb
    98,  // Z=42: 98Mo
    98,  // Z=43: 98Tc
    102, // Z=44: 102Ru
    103, // Z=45: 103Rh
    106, // Z=46: 106Pd
    107, // Z=47: 107Ag
    114, // Z=48: 114Cd
    115, // Z=49: 115In
    120, // Z=50: 120Sn
    121, // Z=51: 121Sb
    130, // Z=52: 130Te
    127, // Z=53: 127I
    132, // Z=54: 132Xe
    133, // Z=55: 133Cs
    138, // Z=56: 138Ba
    139, // Z=57: 139La
    140, // Z=58: 140Ce
    141, // Z=59: 141Pr
    142, // Z=60: 142Nd
    145, // Z=61: 145Pm
    152, // Z=62: 152Sm
    153, // Z=63: 153Eu
    158, // Z=64: 158Gd
    159, // Z=65: 159Tb
    164, // Z=66: 164Dy
    165, // Z=67: 165Ho
    166, // Z=68: 166Er
    169, // Z=69: 169Tm
    174, // Z=70: 174Yb
    175, // Z=71: 175Lu
    180, // Z=72: 180Hf
    181, // Z=73: 181Ta
    184, // Z=74: 184W
    187, // Z=75: 187Re
    192, // Z=76: 192Os
    193, // Z=77: 193Ir
    195, // Z=78: 195Pt
    197, // Z=79: 197Au
    202, // Z=80: 202Hg
    205, // Z=81: 205Tl
    208, // Z=82: 208Pb
    209, // Z=83: 209Bi
    209, // Z=84: 209Po
    210, // Z=85: 210At
    222, // Z=86: 222Rn
    223, // Z=87: 223Fr
    226, // Z=88: 226Ra
    227, // Z=89: 227Ac
    232, // Z=90: 232Th
    231, // Z=91: 231Pa
    238, // Z=92: 238U
    237, // Z=93: 237Np
    244, // Z=94: 244Pu
    243, // Z=95: 243Am
    247, // Z=96: 247Cm
    247, // Z=97: 247Bk
    251, // Z=98: 251Cf
    252, // Z=99: 252Es
    257, // Z=100: 257Fm
    258, // Z=101: 258Md
    259, // Z=102: 259No
    266, // Z=103: 266Lr
    267, // Z=104: 267Rf
    268, // Z=105: 268Db
    269, // Z=106: 269Sg
    270, // Z=107: 270Bh
    277, // Z=108: 277Hs
    278, // Z=109: 278Mt
    281, // Z=110: 281Ds
    282, // Z=111: 282Rg
    285, // Z=112: 285Cn
    286, // Z=113: 286Nh
    289, // Z=114: 289Fl
    290, // Z=115: 290Mc
    293, // Z=116: 293Lv
    294, // Z=117: 294Ts
    294, // Z=118: 294Og
];

/// Seven Madelung period capacities `[2, 8, 8, 18, 18, 32, 32]` summing to `118`
/// (cumulative noble-gas closures `[2, 10, 18, 36, 54, 86, 118]`).
pub const MADELUNG_SHELL_CAPACITIES: [usize; 7] = [2, 8, 8, 18, 18, 32, 32];

/// Look up the IUPAC symbol for `z <= 118` (`None` if `z > 118`).
pub fn element_symbol(z: usize) -> Option<&'static str> {
    ELEMENT_SYMBOLS.get(z).copied()
}

/// Colour channel (`0`, `1`, `2`) of a proper 3-edge-colouring of the `T3` nuclear bond graph.
#[derive(Clone, Copy, PartialEq, Eq, PartialOrd, Ord, Hash, Debug, Serialize, Deserialize)]
pub enum ColourChannel {
    /// Channel 0 (`Red`).
    Red = 0,
    /// Channel 1 (`Green`).
    Green = 1,
    /// Channel 2 (`Blue`).
    Blue = 2,
}

impl ColourChannel {
    /// Channel index `0`, `1`, or `2`.
    pub fn index(self) -> usize {
        self as usize
    }
}

/// Exact `T3` maximum inter-nucleon bond count $M_{\mathrm{T3}}(A)$ (`NucleusBondValence.lean`):
/// `0` for $A \le 1$, `1` for $A = 2$, and $\min(\binom{A}{2}, 3\lfloor A/2 \rfloor)$ for $A \ge 3$.
pub fn max_t3_bonds(mass_number_a: usize) -> usize {
    match mass_number_a {
        0 | 1 => 0,
        2 => 1,
        a => {
            let complete = a * (a - 1) / 2;
            let matching_cap = 3 * (a / 2);
            complete.min(matching_cap)
        }
    }
}

/// Coloured inter-nucleon $\gamma\gamma$ bond edge `(u, v)` (`u < v`) carrying its colour channel
/// and 3-strand $V^3$ junction placement.
#[derive(Clone, PartialEq, Eq, Debug, Serialize, Deserialize)]
pub struct NucleonBondEdge {
    /// Lower nucleon index `0 <= u < v < A`.
    pub nucleon_u: usize,
    /// Higher nucleon index `u < v < A`.
    pub nucleon_v: usize,
    /// Assigned proper edge colour (`Red`, `Green`, `Blue`).
    pub colour: ColourChannel,
    /// Coupled quark strand index `3*u + colour.index()` in nucleon `u`.
    pub strand_u: usize,
    /// Coupled quark strand index `3*v + colour.index()` in nucleon `v`.
    pub strand_v: usize,
    /// Canonical $\gamma\gamma$ $V^3$ bond placement entering nucleon `v` (`3*v - 1` junction site).
    pub bond_word: BraidWord,
}

/// Deterministic `T3` proper 3-edge-coloured inter-nucleon bond graph on $A$ nucleons.
#[derive(Clone, PartialEq, Eq, Debug, Serialize, Deserialize)]
pub struct T3BondGraph {
    /// Mass number $A$ (number of nucleon vertices).
    pub num_nucleons: usize,
    /// Proper 3-edge-coloured bond edges achieving $M_{\mathrm{T3}}(A)$.
    pub edges: Vec<NucleonBondEdge>,
}

fn make_bond_edge(u: usize, v: usize, colour: ColourChannel) -> NucleonBondEdge {
    let (nu, nv) = if u < v { (u, v) } else { (v, u) };
    let c = colour.index();
    // Canonical right-hand entry junction into nucleon `nv` (`3*nv - 1` when `nv >= 1`, Moving
    // strands `(3*nv - 1, 3*nv, 3*nv + 1)` inside `[0, 3*A)`):
    let junction_offset = 3 * nv - 1;
    NucleonBondEdge {
        nucleon_u: nu,
        nucleon_v: nv,
        colour,
        strand_u: 3 * nu + c,
        strand_v: 3 * nv + c,
        bond_word: borromean_baryon_word(junction_offset),
    }
}

/// Construct the canonical connected `T3` proper 3-edge-coloured bond graph on $A$ nucleons in
/// exact $O(A)$ closed form (zero backtracking):
/// - $A \le 1$: empty graph (`0` bonds).
/// - $A = 2$: single `Red` bond `(0, 1)` (`1` bond).
/// - $A = 3$: $K_3$ with `(0,1):Red`, `(1,2):Green`, `(0,2):Blue` (`3` bonds).
/// - $A = 4$: $K_4$ with Tait 1-factorization (`6` bonds).
/// - Even $A = 2m \ge 6$: $2m$-vertex Möbius ladder (even outer cycle alternating `Red`/`Green`,
///   plus $m$ opposite chords `(k, k + m)` coloured `Blue` $\implies 3m$ bonds, cubic Class-1).
/// - Odd $A = 2m + 1 \ge 5$: $2m$-vertex construction above ($A - 1 = 2m \ge 4$) with chord
///   `(0, m):Blue` (or `(0, 3):Blue` at $A = 5$) redirected to pendant bond `(0, 2m):Blue`
///   ($3m = 3\lfloor A/2 \rfloor$ bonds, connected, proper 3-edge-coloured).
pub fn construct_t3_bond_graph(mass_number_a: usize) -> T3BondGraph {
    let mut edges = Vec::with_capacity(max_t3_bonds(mass_number_a));
    match mass_number_a {
        0 | 1 => {}
        2 => {
            edges.push(make_bond_edge(0, 1, ColourChannel::Red));
        }
        3 => {
            edges.push(make_bond_edge(0, 1, ColourChannel::Red));
            edges.push(make_bond_edge(1, 2, ColourChannel::Green));
            edges.push(make_bond_edge(0, 2, ColourChannel::Blue));
        }
        4 => {
            edges.push(make_bond_edge(0, 1, ColourChannel::Red));
            edges.push(make_bond_edge(2, 3, ColourChannel::Red));
            edges.push(make_bond_edge(0, 2, ColourChannel::Green));
            edges.push(make_bond_edge(1, 3, ColourChannel::Green));
            edges.push(make_bond_edge(0, 3, ColourChannel::Blue));
            edges.push(make_bond_edge(1, 2, ColourChannel::Blue));
        }
        5 => {
            // Take K_4 (6 edges), replace (0, 3, Blue) with (0, 4, Blue):
            // Remaining on 0..3: (0,1,R), (2,3,R), (0,2,G), (1,3,G), (1,2,B) -> connected, plus (0,4,B)!
            edges.push(make_bond_edge(0, 1, ColourChannel::Red));
            edges.push(make_bond_edge(2, 3, ColourChannel::Red));
            edges.push(make_bond_edge(0, 2, ColourChannel::Green));
            edges.push(make_bond_edge(1, 3, ColourChannel::Green));
            edges.push(make_bond_edge(1, 2, ColourChannel::Blue));
            edges.push(make_bond_edge(0, 4, ColourChannel::Blue));
        }
        a if a % 2 == 0 => {
            let m = a / 2;
            // Even cycle 0..2m alternating Red and Green:
            for k in 0..a {
                let col = if k % 2 == 0 {
                    ColourChannel::Red
                } else {
                    ColourChannel::Green
                };
                edges.push(make_bond_edge(k, (k + 1) % a, col));
            }
            // Main diagonals (k, k + m) coloured Blue:
            for k in 0..m {
                edges.push(make_bond_edge(k, k + m, ColourChannel::Blue));
            }
        }
        a => {
            // Odd A = 2m + 1 >= 7: start from 2m-vertex Mobius ladder, redirect (0, m, Blue) -> (0, 2m, Blue):
            let even_n = a - 1;
            let m = even_n / 2;
            for k in 0..even_n {
                let col = if k % 2 == 0 {
                    ColourChannel::Red
                } else {
                    ColourChannel::Green
                };
                edges.push(make_bond_edge(k, (k + 1) % even_n, col));
            }
            edges.push(make_bond_edge(0, even_n, ColourChannel::Blue));
            for k in 1..m {
                edges.push(make_bond_edge(k, k + m, ColourChannel::Blue));
            }
        }
    }

    edges.sort_by_key(|e| (e.nucleon_u, e.nucleon_v));
    T3BondGraph {
        num_nucleons: mass_number_a,
        edges,
    }
}

/// Verify all invariants of a `T3BondGraph`:
/// 1. Exact edge count `edges.len() == max_t3_bonds(A)`,
/// 2. Simple undirected edges (`0 <= u < v < A`, no duplicate pairs),
/// 3. Maximum degree $\le 3$ and proper 3-edge-colouring (no vertex has two incident edges of the same colour),
/// 4. Connectedness across all $A$ vertices whenever $A \ge 1$.
pub fn verify_t3_bond_graph(graph: &T3BondGraph) -> Result<(), String> {
    let a = graph.num_nucleons;
    let expected = max_t3_bonds(a);
    if graph.edges.len() != expected {
        return Err(format!(
            "A={a}: edge count {} != max_t3_bonds({a}) = {expected}",
            graph.edges.len()
        ));
    }

    let mut seen_pairs = BTreeSet::new();
    let mut colour_used = vec![[false; 3]; a];
    let mut adj: Vec<Vec<usize>> = vec![Vec::new(); a];

    for e in &graph.edges {
        if e.nucleon_u >= e.nucleon_v || e.nucleon_v >= a {
            return Err(format!(
                "A={a}: invalid edge endpoints ({}, {})",
                e.nucleon_u, e.nucleon_v
            ));
        }
        if !seen_pairs.insert((e.nucleon_u, e.nucleon_v)) {
            return Err(format!(
                "A={a}: duplicate edge ({}, {})",
                e.nucleon_u, e.nucleon_v
            ));
        }
        let c = e.colour.index();
        if colour_used[e.nucleon_u][c] {
            return Err(format!(
                "A={a}: colour {:?} used twice at nucleon {}",
                e.colour, e.nucleon_u
            ));
        }
        if colour_used[e.nucleon_v][c] {
            return Err(format!(
                "A={a}: colour {:?} used twice at nucleon {}",
                e.colour, e.nucleon_v
            ));
        }
        colour_used[e.nucleon_u][c] = true;
        colour_used[e.nucleon_v][c] = true;
        adj[e.nucleon_u].push(e.nucleon_v);
        adj[e.nucleon_v].push(e.nucleon_u);
    }

    if a >= 2 {
        let mut visited = vec![false; a];
        let mut q = VecDeque::new();
        visited[0] = true;
        q.push_back(0);
        let mut reached = 1usize;
        while let Some(u) = q.pop_front() {
            for &v in &adj[u] {
                if !visited[v] {
                    visited[v] = true;
                    reached += 1;
                    q.push_back(v);
                }
            }
        }
        if reached != a {
            return Err(format!(
                "A={a}: T3 bond graph disconnected (reached {reached} of {a} nucleons)"
            ));
        }
    }
    Ok(())
}

/// Placement metadata for a single nucleon inside an `AtomicDatum`.
#[derive(Clone, PartialEq, Eq, Debug, Serialize, Deserialize)]
pub struct NucleonPlacement {
    /// Nucleon index `0 <= index < A`.
    pub index: usize,
    /// Nucleon isospin species (`Proton` or `Neutron`).
    pub kind: NucleonKind,
    /// Valence quark flavours (`uud` or `udd`).
    pub flavours: [QuarkFlavour; 3],
    /// Assigned quark strand triple `[3*index, 3*index + 1, 3*index + 2]`.
    pub quark_strands: [usize; 3],
    /// Intra-nucleon Borromean core word $\beta_{\mathrm{Bor}}^{(3k)} = V_{3k}^3$.
    pub core_word: BraidWord,
}

/// Madelung shell occupancy and Hopf crossing placement for bound atomic electrons.
#[derive(Clone, PartialEq, Eq, Debug, Serialize, Deserialize)]
pub struct ElectronShellPlacement {
    /// 1-based Madelung period index `1..=7`.
    pub period_index: usize,
    /// Pauli period capacity (`2, 8, 8, 18, 18, 32, 32`).
    pub shell_capacity: usize,
    /// Number of electrons occupying this period (`1 <= occupancy <= shell_capacity`).
    pub occupancy: usize,
    /// Electron strand range `[strand_start, strand_start + occupancy)` above the $3A$ nuclear strands.
    pub strand_start: usize,
    /// Per-electron ruled Hopf braid placements ($\sigma_s\sigma_{s+1}\sigma_s$).
    pub hopf_words: Vec<BraidWord>,
}

/// Complete serializable $(Z, N)$ nuclear + electronic $\gamma\gamma$ atomic datum.
#[derive(Clone, PartialEq, Eq, Debug, Serialize, Deserialize)]
pub struct AtomicDatum {
    /// Atomic (proton) number $Z \in \{0, \dots, 118\}$.
    pub z_protons: usize,
    /// Neutron count $N \ge 0$.
    pub n_neutrons: usize,
    /// Mass number $A = Z + N$.
    pub a_mass: usize,
    /// IUPAC symbol (`"n"` for $Z = 0$, `"H"`..`"Og"` for $Z = 1..118$).
    pub symbol: String,
    /// Total nuclear quark strands $3A$.
    pub nuclear_quark_strands: usize,
    /// Total bound electron strands $Z$ (for neutral atom).
    pub electron_strands: usize,
    /// Ambient total braid strand count ($\max(3A + Z + 2, 3)$ when $Z > 0$, else $3A$).
    pub total_braid_strands: usize,
    /// Ordered nucleon placements (`0..A`, canonically alternating proton/neutron to maximize isospin mixing).
    pub nucleons: Vec<NucleonPlacement>,
    /// Deterministic `T3` proper 3-edge-coloured inter-nucleon bond graph.
    pub bond_graph: T3BondGraph,
    /// Madelung `2n²` period placements for the $Z$ atomic electrons.
    pub electron_shells: Vec<ElectronShellPlacement>,
}

impl AtomicDatum {
    /// Serialize this `AtomicDatum` to canonical pretty JSON.
    pub fn to_json_pretty(&self) -> Result<String, serde_json::Error> {
        serde_json::to_string_pretty(self)
    }

    /// Deserialize an `AtomicDatum` from JSON text.
    pub fn from_json_str(json: &str) -> Result<Self, serde_json::Error> {
        serde_json::from_str(json)
    }

    /// Concatenate all intra-nucleon $V^3$ cores followed by all `T3` inter-nucleon $V^3$ bond words
    /// into a single nuclear $\gamma\gamma$ `BraidWord` on `3 * A` strands.
    pub fn nuclear_braid_word(&self) -> BraidWord {
        let mut out = BraidWord::empty();
        for nuc in &self.nucleons {
            out = out.concat(&nuc.core_word);
        }
        for edge in &self.bond_graph.edges {
            out = out.concat(&edge.bond_word);
        }
        out
    }
}

/// Build the deterministic canonical `AtomicDatum` for any $(Z, N)$ with $Z \le 118$ and $A = Z + N \ge 1$.
pub fn build_atomic_datum(z_protons: usize, n_neutrons: usize) -> AtomicDatum {
    assert!(
        z_protons <= 118,
        "atomic number Z={z_protons} exceeds supported chart Z <= 118"
    );
    let a_mass = z_protons + n_neutrons;
    assert!(a_mass >= 1, "mass number A = Z + N must be >= 1");

    let symbol = element_symbol(z_protons).unwrap_or("Unknown").to_string();

    // Deterministic interleaving of Z protons and N neutrons across indices 0..A:
    let mut nucleons = Vec::with_capacity(a_mass);
    let mut rem_p = z_protons;
    let mut rem_n = n_neutrons;
    for idx in 0..a_mass {
        let pick_proton = if rem_p == 0 {
            false
        } else if rem_n == 0 {
            true
        } else {
            rem_p >= rem_n
        };
        let kind = if pick_proton {
            rem_p -= 1;
            NucleonKind::Proton
        } else {
            rem_n -= 1;
            NucleonKind::Neutron
        };
        nucleons.push(NucleonPlacement {
            index: idx,
            kind,
            flavours: kind.valence_flavours(),
            quark_strands: [3 * idx, 3 * idx + 1, 3 * idx + 2],
            core_word: borromean_baryon_word(3 * idx),
        });
    }

    let bond_graph = construct_t3_bond_graph(a_mass);
    let nuclear_quark_strands = 3 * a_mass;

    // Fill Madelung shells [2, 8, 8, 18, 18, 32, 32] up to Z electrons:
    let mut electron_shells = Vec::new();
    let mut rem_e = z_protons;
    let mut cur_strand = nuclear_quark_strands;
    for (p_idx, &cap) in MADELUNG_SHELL_CAPACITIES.iter().enumerate() {
        if rem_e == 0 {
            break;
        }
        let occ = rem_e.min(cap);
        let mut hopf_words = Vec::with_capacity(occ);
        for e_local in 0..occ {
            let offset = if cur_strand + e_local >= 1 {
                cur_strand + e_local - 1
            } else {
                0
            };
            hopf_words.push(electron_hopf_word(offset));
        }
        electron_shells.push(ElectronShellPlacement {
            period_index: p_idx + 1,
            shell_capacity: cap,
            occupancy: occ,
            strand_start: cur_strand,
            hopf_words,
        });
        cur_strand += occ;
        rem_e -= occ;
    }

    let total_braid_strands = if z_protons == 0 {
        nuclear_quark_strands
    } else {
        (nuclear_quark_strands + z_protons + 1).max(3)
    };

    AtomicDatum {
        z_protons,
        n_neutrons,
        a_mass,
        symbol,
        nuclear_quark_strands,
        electron_strands: z_protons,
        total_braid_strands,
        nucleons,
        bond_graph,
        electron_shells,
    }
}

/// Generate the complete 119-element canonical atomic chart (`Z = 0..=118`) at valley-of-stability
/// neutron counts (`CANONICAL_MASS_NUMBERS[Z] - Z`).
pub fn canonical_atomic_chart_0_to_118() -> Vec<AtomicDatum> {
    (0..=118)
        .map(|z| {
            let a = CANONICAL_MASS_NUMBERS[z];
            build_atomic_datum(z, a - z)
        })
        .collect()
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn t3_bond_graph_verified_exhaustively_up_to_a300() {
        // Exact K_A values at A = 2, 3, 4 and 3*floor(A/2) for A >= 4:
        assert_eq!(max_t3_bonds(0), 0);
        assert_eq!(max_t3_bonds(1), 0);
        assert_eq!(max_t3_bonds(2), 1);
        assert_eq!(max_t3_bonds(3), 3);
        assert_eq!(max_t3_bonds(4), 6);
        assert_eq!(max_t3_bonds(5), 6);
        assert_eq!(max_t3_bonds(6), 9);
        assert_eq!(max_t3_bonds(7), 9);
        assert_eq!(max_t3_bonds(8), 12);

        for a in 0..=300 {
            let g = construct_t3_bond_graph(a);
            verify_t3_bond_graph(&g).unwrap_or_else(|err| panic!("failed at A={a}: {err}"));
        }
    }

    #[test]
    fn full_atomic_chart_z0_to_z118_builds_and_roundtrips_json() {
        let chart = canonical_atomic_chart_0_to_118();
        assert_eq!(chart.len(), 119);

        // Verify neutron (0,1), 1H (1,0), 4He (2,2), 12C (6,6), 56Fe (26,30), 208Pb (82,126), 294Og (118,176):
        assert_eq!(chart[0].symbol, "n");
        assert_eq!(chart[0].a_mass, 1);
        assert_eq!(chart[0].electron_shells.len(), 0);

        assert_eq!(chart[1].symbol, "H");
        assert_eq!(chart[1].a_mass, 1);
        assert_eq!(chart[1].electron_strands, 1);

        assert_eq!(chart[2].symbol, "He");
        assert_eq!(chart[2].bond_graph.edges.len(), 6); // K_4 on alpha particle!

        assert_eq!(chart[6].symbol, "C");
        assert_eq!(chart[6].bond_graph.edges.len(), 18); // 3 * (12 / 2) = 18

        assert_eq!(chart[118].symbol, "Og");
        assert_eq!(chart[118].a_mass, 294);
        assert_eq!(chart[118].nuclear_quark_strands, 882);
        assert_eq!(chart[118].electron_shells.len(), 7);
        let total_e: usize = chart[118]
            .electron_shells
            .iter()
            .map(|s| s.occupancy)
            .sum();
        assert_eq!(total_e, 118);

        for datum in &chart {
            verify_t3_bond_graph(&datum.bond_graph).unwrap();
            let p_count = datum
                .nucleons
                .iter()
                .filter(|n| n.kind == NucleonKind::Proton)
                .count();
            let n_count = datum
                .nucleons
                .iter()
                .filter(|n| n.kind == NucleonKind::Neutron)
                .count();
            assert_eq!(p_count, datum.z_protons);
            assert_eq!(n_count, datum.n_neutrons);
        }

        // JSON round-trip on Deuteron (1,1) and Oganesson (118,176):
        let deuteron = build_atomic_datum(1, 1);
        let d_json = deuteron.to_json_pretty().unwrap();
        assert_eq!(AtomicDatum::from_json_str(&d_json).unwrap(), deuteron);

        let og_json = chart[118].to_json_pretty().unwrap();
        assert_eq!(AtomicDatum::from_json_str(&og_json).unwrap(), chart[118]);
    }
}
