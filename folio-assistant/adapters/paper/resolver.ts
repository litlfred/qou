/**
 * Paper adapter — Content resolution (folio, paper, chapter, section, block).
 *
 * Resolves .ts manifests + .md content + .lean source from disk or git branches.
 *
 * @module folio-assistant/adapters/paper/resolver
 */

import { existsSync, readFileSync, readdirSync } from "fs";
import { join, resolve } from "path";
import type { GitHelper } from "../../src/core/git.js";
import type { FeedbackStore } from "../../src/core/feedback.js";
import { TtlCache } from "../../src/core/cache.js";
import type {
  FolioItem,
  ContentOutline,
  OutlineChapter,
  ResolvedBlock,
  ResolvedSection,
  ResolvedChapter,
  ResolvedDocument,
  ChapterDetail,
  SectionStub,
} from "../../src/types.js";

export class PaperResolver {
  private outlineCache = new TtlCache<ContentOutline>();
  private chapterCache = new TtlCache<ChapterDetail>();
  private sectionCache = new TtlCache<ResolvedSection>();
  private documentCache = new TtlCache<ResolvedDocument & { branch: string }>();

  constructor(
    private repoRoot: string,
    private gitHelper: GitHelper,
    private feedbackStore: FeedbackStore,
  ) {}

  invalidateCache(itemId?: string): void {
    if (itemId) {
      const prefix = itemId + ":";
      this.outlineCache.invalidate(prefix);
      this.chapterCache.invalidate(prefix);
      this.sectionCache.invalidate(prefix);
      this.documentCache.invalidate(prefix);
    } else {
      this.outlineCache.invalidate();
      this.chapterCache.invalidate();
      this.sectionCache.invalidate();
      this.documentCache.invalidate();
    }
  }

  // ── Folio listing ──────────────────────────────────────────────

  async resolveFolio(branch?: string): Promise<{ title: string; items: FolioItem[]; branch: string }> {
    const br = branch;
    const folioRel = "content/folio.ts";
    let folioData: { title: string; papers: Array<{ dir: string; title?: string; description?: string; tags?: string[] }> };

    if (this.gitHelper.fileExistsBranch(br, folioRel)) {
      folioData = (await this.gitHelper.importTsBranch(br, folioRel)) as any;
    } else {
      const dirs = this.gitHelper.listDirBranch(br, "content").filter((d) => {
        if (d === "schema" || d === "pipeline" || d === "node_modules") return false;
        return this.gitHelper.fileExistsBranch(br, `content/${d}/${d}.ts`);
      });
      folioData = { title: "Documents", papers: dirs.map((d) => ({ dir: d })) };
    }

    const items: FolioItem[] = [];
    for (const ref of folioData.papers) {
      try {
        const paperMod = (await this.gitHelper.importTsBranch(br, `content/${ref.dir}/${ref.dir}.ts`)) as any;
        let blockCount = 0, provedCount = 0, todoCount = 0, chapCount = 0;

        for (const chRef of paperMod.chapters || []) {
          const chRel = `content/${ref.dir}/${chRef.dir}/${chRef.dir}.ts`;
          if (!this.gitHelper.fileExistsBranch(br, chRel)) continue;
          chapCount++;
          const ch = (await this.gitHelper.importTsBranch(br, chRel)) as any;
          for (const sec of ch.sections || []) {
            if (!("blocks" in sec)) continue;
            for (const rootName of sec.blocks) {
              const blkRel = `content/${ref.dir}/${chRef.dir}/${rootName}.ts`;
              if (!this.gitHelper.fileExistsBranch(br, blkRel)) continue;
              blockCount++;
              try {
                const blk = (await this.gitHelper.importTsBranch(br, blkRel)) as any;
                if (blk.status === "proved" || blk.status === "mathlib_ok") provedCount++;
                const fb = this.feedbackStore.read(ref.dir, rootName);
                if (fb.length) todoCount += fb.filter((t: any) => t.status !== "resolved" && t.status !== "wontfix").length;
              } catch {}
            }
          }
        }

        items.push({
          id: ref.dir,
          title: ref.title || paperMod.title,
          description: ref.description,
          tags: ref.tags,
          authors: paperMod.authors,
          date: paperMod.date,
          stats: { chapters: chapCount, blocks: blockCount, proved: provedCount, todos: todoCount },
        });
      } catch (e) {
        items.push({
          id: ref.dir,
          title: ref.title || ref.dir,
          description: ref.description,
          tags: ref.tags,
          authors: [],
          stats: { chapters: 0, blocks: 0, proved: 0, todos: 0 },
        });
      }
    }

    return { title: folioData.title, items, branch: this.gitHelper.currentBranch() };
  }

  // ── Paper outline ──────────────────────────────────────────────

  async resolveOutline(id: string, branch?: string): Promise<ContentOutline | null> {
    const cacheKey = `${id}:${branch || "HEAD"}`;
    const cached = this.outlineCache.get(cacheKey);
    if (cached) return cached;

    const br = branch;
    const paperRel = `content/${id}/${id}.ts`;
    if (!this.gitHelper.fileExistsBranch(br, paperRel)) return null;

    const paperMod = (await this.gitHelper.importTsBranch(br, paperRel)) as any;
    const chapters: OutlineChapter[] = [];

    for (const chRef of paperMod.chapters || []) {
      const chTsRel = `content/${id}/${chRef.dir}/${chRef.dir}.ts`;
      if (!this.gitHelper.fileExistsBranch(br, chTsRel)) continue;
      const ch = (await this.gitHelper.importTsBranch(br, chTsRel)) as any;

      const sections: OutlineChapter["sections"] = [];
      for (const sec of ch.sections || []) {
        if ("name" in sec && !("blocks" in sec)) continue;
        const section = sec as { title: string; label?: string; blocks: string[] };
        sections.push({ title: section.title, label: section.label, blockCount: section.blocks.length });
      }

      chapters.push({ number: ch.number, title: ch.title, label: ch.label, dir: chRef.dir, sections });
    }

    const result: ContentOutline = {
      id,
      title: paperMod.title,
      authors: paperMod.authors,
      affiliations: paperMod.affiliations,
      date: paperMod.date,
      chapters,
      branch: this.gitHelper.currentBranch(),
    };

    this.outlineCache.set(cacheKey, result);
    return result;
  }

  // ── Chapter detail ─────────────────────────────────────────────

  async resolveChapterDetail(paperId: string, chapterDir: string, branch?: string): Promise<ChapterDetail | null> {
    const cacheKey = `${paperId}:${branch || "HEAD"}:ch:${chapterDir}`;
    const cached = this.chapterCache.get(cacheKey);
    if (cached) return cached;

    const br = branch;
    const chRel = `content/${paperId}/${chapterDir}`;
    const chTsRel = `${chRel}/${chapterDir}.ts`;
    if (!this.gitHelper.fileExistsBranch(br, chTsRel)) return null;

    const ch = (await this.gitHelper.importTsBranch(br, chTsRel)) as any;
    const sections: SectionStub[] = [];

    for (const sec of ch.sections || []) {
      if ("name" in sec && !("blocks" in sec)) continue;
      const section = sec as { title: string; label?: string; blocks: string[] };

      const blockStubs: SectionStub["blockStubs"] = [];
      for (const rootName of section.blocks) {
        const blkTsRel = `${chRel}/${rootName}.ts`;
        try {
          const blk = (await this.gitHelper.importTsBranch(br, blkTsRel)) as any;
          const feedback = this.feedbackStore.read(paperId, rootName);
          blockStubs.push({
            rootName,
            kind: blk.kind,
            label: blk.label,
            title: blk.title,
            status: blk.status,
            lean: blk.lean ? { decl: blk.lean.decl, file: blk.lean.file, validation: blk.lean.validation } : undefined,
            todoCount: feedback.filter((t: any) => t.status === "open").length,
          });
        } catch {
          blockStubs.push({ rootName, kind: "error", todoCount: 0 });
        }
      }

      sections.push({ title: section.title, label: section.label, blockCount: section.blocks.length, blockStubs });
    }

    const chTodos = this.feedbackStore.read(paperId, `__chapter:${chapterDir}`);
    const result: ChapterDetail = {
      number: ch.number,
      title: ch.title,
      label: ch.label,
      dir: chapterDir,
      sections,
      todos: chTodos.length ? chTodos : undefined,
    };

    this.chapterCache.set(cacheKey, result);
    return result;
  }

  // ── Section (full blocks with md/lean) ─────────────────────────

  async resolveSection(paperId: string, chapterDir: string, sectionIndex: number, branch?: string): Promise<ResolvedSection | null> {
    const cacheKey = `${paperId}:${branch || "HEAD"}:sec:${chapterDir}:${sectionIndex}`;
    const cached = this.sectionCache.get(cacheKey);
    if (cached) return cached;

    const br = branch;
    const chRel = `content/${paperId}/${chapterDir}`;
    const chTsRel = `${chRel}/${chapterDir}.ts`;
    if (!this.gitHelper.fileExistsBranch(br, chTsRel)) return null;

    const ch = (await this.gitHelper.importTsBranch(br, chTsRel)) as any;
    const realSections = (ch.sections || []).filter((s: any) => !("name" in s && !("blocks" in s)));
    if (sectionIndex < 0 || sectionIndex >= realSections.length) return null;

    const sec = realSections[sectionIndex] as { title: string; label?: string; blocks: string[] };
    const blocks = await this.resolveBlocks(paperId, chRel, sec.blocks, br);

    const result: ResolvedSection = { title: sec.title, label: sec.label, blocks };
    this.sectionCache.set(cacheKey, result);
    return result;
  }

  // ── Full document ──────────────────────────────────────────────

  async resolveDocument(id: string, branch?: string): Promise<(ResolvedDocument & { branch: string }) | null> {
    const cacheKey = `${id}:${branch || "HEAD"}`;
    const cached = this.documentCache.get(cacheKey);
    if (cached) return cached;

    const br = branch;
    const paperRel = `content/${id}/${id}.ts`;
    if (!this.gitHelper.fileExistsBranch(br, paperRel)) return null;

    const paperMod = (await this.gitHelper.importTsBranch(br, paperRel)) as any;
    const chapters: ResolvedChapter[] = [];

    for (const chRef of paperMod.chapters || []) {
      const chRel = `content/${id}/${chRef.dir}`;
      const chTsRel = `${chRel}/${chRef.dir}.ts`;
      if (!this.gitHelper.fileExistsBranch(br, chTsRel)) continue;
      const ch = (await this.gitHelper.importTsBranch(br, chTsRel)) as any;

      const sections: ResolvedSection[] = [];
      for (const sec of ch.sections || []) {
        if ("name" in sec && !("blocks" in sec)) continue;
        const section = sec as { title: string; label?: string; blocks: string[] };
        const blocks = await this.resolveBlocks(id, chRel, section.blocks, br);
        sections.push({ title: section.title, label: section.label, blocks });
      }

      const chTodos = this.feedbackStore.read(id, `__chapter:${chRef.dir}`);
      chapters.push({
        number: ch.number,
        title: ch.title,
        label: ch.label,
        sections,
        todos: chTodos.length ? chTodos : undefined,
      });
    }

    const blocksByName = new Map<string, ResolvedBlock>();
    for (const ch of chapters)
      for (const sec of ch.sections)
        for (const blk of sec.blocks)
          blocksByName.set(blk.rootName, blk);

    const paperTodos = this.feedbackStore.read(id, "__paper");
    const result = {
      id,
      title: paperMod.title,
      authors: paperMod.authors,
      affiliations: paperMod.affiliations,
      date: paperMod.date,
      macros: paperMod.macros,
      chapters,
      todos: paperTodos.length ? paperTodos : undefined,
      branch: this.gitHelper.currentBranch(),
      blocksByName,
    };

    this.documentCache.set(cacheKey, result);
    return result;
  }

  // ── Block resolution (shared by section + document) ────────────

  private async resolveBlocks(
    paperId: string,
    chRel: string,
    blockNames: string[],
    branch?: string,
  ): Promise<ResolvedBlock[]> {
    const br = branch;
    const blocks: ResolvedBlock[] = [];
    const leanDir = resolve(this.repoRoot, "lean");

    for (const rootName of blockNames) {
      const blkTsRel = `${chRel}/${rootName}.ts`;
      const blkMdRel = `${chRel}/${rootName}.md`;
      try {
        const blk = (await this.gitHelper.importTsBranch(br, blkTsRel)) as any;
        const md = this.gitHelper.readFileBranch(br, blkMdRel) || "";

        const feedback = this.feedbackStore.read(paperId, rootName);
        const blockTodos = feedback.length ? [...feedback] : undefined;

        // Read Lean source if available
        let leanSource: string | undefined;
        if (blk.lean) {
          if (blk.lean.file) {
            leanSource = this.gitHelper.readFileBranch(br, `lean/${blk.lean.file}`) ?? undefined;
          }
          if (!leanSource) {
            leanSource = this.gitHelper.readFileBranch(br, `${chRel}/${rootName}.lean`) ?? undefined;
          }
          if (!leanSource && blk.lean.decl) {
            const parts = blk.lean.decl.split(".");
            for (let i = parts.length; i >= 2; i--) {
              const candidate = `lean/${parts.slice(0, i).join("/")}.lean`;
              leanSource = this.gitHelper.readFileBranch(br, candidate) ?? undefined;
              if (leanSource) break;
            }
          }
          // Grep fallback for current branch only
          if (!leanSource && blk.lean.decl && this.gitHelper.isCurrentBranch(br)) {
            const declName = blk.lean.decl.split(".").pop() || "";
            try {
              const leanSrcDir = join(leanDir, "QOU");
              if (existsSync(leanSrcDir)) {
                const result = Bun.spawnSync(["grep", "-rl", declName, leanSrcDir]);
                const files = result.stdout.toString().trim().split("\n").filter(Boolean);
                if (files.length > 0 && existsSync(files[0])) {
                  leanSource = readFileSync(files[0], "utf-8");
                }
              }
            } catch {}
          }
        }

        const rendered = blk.rendered?.map(
          (r: { mime: string; url: string; blockIndex: number; hash?: string }) => ({
            ...r,
            url: `/api/content-asset/${paperId}/${chRel.split("/").pop()}/${r.url}`,
          }),
        );

        blocks.push({
          rootName,
          kind: blk.kind,
          label: blk.label,
          title: blk.title,
          uses: blk.uses,
          examples: blk.examples,
          proofs: blk.proofs,
          lean: blk.lean ? { ...blk.lean, source: leanSource } : undefined,
          status: blk.status,
          tex: blk.tex,
          caption: blk.caption,
          tags: blk.tags,
          rendered,
          md,
          todos: blockTodos,
        });
      } catch (e) {
        blocks.push({ rootName, kind: "error", md: `Failed to load ${rootName}: ${e}` });
      }
    }

    return blocks;
  }
}
