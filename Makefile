# Dataset tasks for bioamla-datasets. Each target wraps a `bioamla dataset`
# command; set DS=<name> to pick a directory under datasets/ (default esc-50).
# Use BIOAMLA='uv run --project ~/repos/laborae/projects/bioamla bioamla' to
# run against a development checkout instead of the installed package.

.DEFAULT_GOAL := help
.PHONY: help stats license manifest push remix lfs-check

BIOAMLA ?= bioamla
DS      ?= esc-50
DIR      = datasets/$(DS)
TEMPLATE ?= templates/$(if $(filter esc-50,$(DS)),esc50_license_template,license_template)
HF_REPO ?= bioamla/$(DS)

help: ## Show available targets
	@grep -E '^[a-zA-Z_-]+:.*?## ' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "  \033[36m%-10s\033[0m %s\n", $$1, $$2}'
	@echo; echo "  DS=$(DS)  BIOAMLA=$(BIOAMLA)"

stats: ## Summarise $(DIR)/metadata.csv
	@$(BIOAMLA) dataset stats $(DIR)

license: ## Regenerate $(DIR)/LICENSE from metadata (TEMPLATE=... to override the header)
	@$(BIOAMLA) dataset license $(DIR) -t $(TEMPLATE) -o LICENSE

manifest: ## Write $(DIR)/dataset.json (label vocabulary, counts, splits)
	@$(BIOAMLA) dataset manifest $(DIR)

push: ## Push $(DIR) to Hugging Face as $(HF_REPO), keeping its README (PRIVATE=1 for a private repo)
	@$(BIOAMLA) catalogs hf push-dataset $(DIR) $(HF_REPO) --no-card $(if $(PRIVATE),--private,--public)


remix: ## Build build/<NAME> from remixes/<NAME>.toml: make remix NAME=esc-50-animals
	@test -n "$(NAME)" || { echo "usage: make remix NAME=<recipe>"; exit 1; }
	@test -f remixes/$(NAME).toml || { echo "no recipe remixes/$(NAME).toml"; exit 1; }
	@rm -rf build/$(NAME)
	@$(BIOAMLA) dataset remix build/$(NAME) --recipe remixes/$(NAME).toml -t $(TEMPLATE)

lfs-check: ## Confirm audio files are real LFS content, not pointers
	@n=$$(git lfs ls-files | wc -l | tr -d ' '); p=$$(grep -rl --include='*.wav' '^version https://git-lfs' datasets 2>/dev/null | wc -l | tr -d ' '); \
	echo "LFS-tracked files: $$n, unresolved pointers: $$p"; test "$$p" -eq 0 || { echo "run: git lfs pull"; exit 1; }
