// sample code from commit.c of the Git repository (https://github.com/git)

struct commit *lookup_commit_or_die(const unsigned char *sha1, const char *ref_name)
{
	struct commit *c = lookup_commit_reference(sha1);
	if (!c)
		die(_("could not parse %s"), ref_name);
	if (hashcmp(sha1, c->object.sha1)) {
		warning(_("%s %s is not a commit!"),
			ref_name, sha1_to_hex(sha1));
	}
	return c;
}
