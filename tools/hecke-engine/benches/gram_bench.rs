use criterion::{black_box, criterion_group, criterion_main, Criterion};
use hecke_engine::{atom, gram, nf};

fn bench_gram_matrix(c: &mut Criterion) {
    c.bench_function("gram_matrix(Q_0)", |b| {
        b.iter(|| gram::gram_matrix(black_box(nf::Q_0)))
    });
}

fn bench_gram_inverse(c: &mut Criterion) {
    c.bench_function("gram_inverse(Q_0)", |b| {
        b.iter(|| gram::gram_inverse(black_box(nf::Q_0)))
    });
}

fn bench_build_atom_nf(c: &mut Criterion) {
    let h = nf::hecke_h(nf::Q_0);
    let mut group = c.benchmark_group("build_atom_nf");
    for (z, n) in [(1u32, 0u32), (2, 2), (6, 6), (8, 8)] {
        group.bench_function(format!("Z={},N={}", z, n), |b| {
            b.iter(|| atom::build_atom_nf(black_box(z), black_box(n), black_box(h)))
        });
    }
    group.finish();
}

fn bench_atom_volumes(c: &mut Criterion) {
    c.bench_function("atom_per_generator_volumes(6,6)", |b| {
        b.iter(|| {
            atom::atom_per_generator_volumes(
                black_box(6), black_box(6), true, 1, None, None, None,
                black_box(nf::Q_0),
            )
        })
    });
}

/// Build a large, pre-mul'd polynomial that exercises `reduce_nf`
/// against many word-rewrite triggers. This is the workload that
/// the SmallVec + buffer-reuse changes actually optimize (the 6×6
/// Gram path reduces very short words and hides the speedup).
fn bench_reduce_nf_heavy(c: &mut Criterion) {
    let h = nf::hecke_h(nf::Q_0);

    // Build a "heavy" input: multiply the NF basis with itself twice,
    // yielding words of length up to 6 before reduction. This is the
    // pattern the GB-NF loop hits when reducing repeated basis
    // products.
    let mut heavy = nf::Poly::default();
    for i in 0..6 {
        for j in 0..6 {
            for k in 0..6 {
                let ab = nf::mul_polys(&nf::poly_from(i), &nf::poly_from(j));
                let abc = nf::mul_polys(&ab, &nf::poly_from(k));
                for (w, c) in abc {
                    heavy.entry(w).and_modify(|v| *v += c).or_insert(c);
                }
            }
        }
    }

    c.bench_function("reduce_nf(heavy)", |b| {
        b.iter(|| nf::reduce_nf(black_box(heavy.clone()), black_box(h)))
    });
}

criterion_group!(
    benches,
    bench_gram_matrix,
    bench_gram_inverse,
    bench_build_atom_nf,
    bench_atom_volumes,
    bench_reduce_nf_heavy,
);
criterion_main!(benches);
