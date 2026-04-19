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

criterion_group!(
    benches,
    bench_gram_matrix,
    bench_gram_inverse,
    bench_build_atom_nf,
    bench_atom_volumes
);
criterion_main!(benches);
