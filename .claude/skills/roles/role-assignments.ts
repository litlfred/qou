import type { RoleAssignment } from "../framework/types.js";

/**
 * Role assignment rules, evaluated in priority order (highest first).
 * The first matching rule determines the actor.
 */
export const roleAssignments: RoleAssignment[] = [
  {
    userPattern: "litlfred",
    identitySource: "git-config",
    actorId: "owner",
    priority: 100,
  },
  {
    userPattern: "litlfred",
    identitySource: "github-oauth",
    actorId: "owner",
    priority: 100,
  },
  {
    userPattern: "*",
    identitySource: "github-oauth",
    actorId: "collaborator",
    priority: 50,
  },
  {
    userPattern: "*",
    identitySource: "bearer-token",
    actorId: "collaborator",
    priority: 40,
  },
  {
    userPattern: "*",
    identitySource: "google-oauth",
    actorId: "reader",
    priority: 30,
  },
  {
    userPattern: "*",
    identitySource: "default",
    actorId: "reader",
    priority: 0,
  },
];
