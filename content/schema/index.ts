/**
 * Content schema — public API (re-exports from schemas/).
 *
 * @example
 *   import { definition, theorem, prose } from "./schema";
 *   import type { Block, Chapter, Document } from "./schema";
 */
export * from "../../folio-assistant/cat-harness/schemas/index";

// Bibliography (CSL-JSON source of truth)
export {
  references,
  referenceMap,
  ref,
  getRef,
  allRefIds,
  CSLEntrySchema,
  CSLItemTypeSchema,
} from "./references";
export type { CSLData, CSLPerson, CSLDate, ItemType } from "./references";
