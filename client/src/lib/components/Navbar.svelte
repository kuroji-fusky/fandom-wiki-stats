<script lang="ts">
  import { PlusIcon, SearchIcon, EllipsisVerticalIcon } from "lucide-svelte"
</script>

<nav class="flex justify-between items-center px-4 lg:px-6 py-4">
  <div translate="no">
    <div>FWS</div>
    <span>
      by
      <a href="https://fusky.pet/" target="_blank">Kuroji Fusky</a>
    </span>
  </div>
  <div class="flex justify-between items-center">
    <button class="py-1.5 px-2.5 inline-flex items-center" aria-label="Create">
      <PlusIcon size={21} />
      <span>Create</span>
    </button>
    <button class="p-1.5" aria-label="Search for wikis">
      <SearchIcon size={20} />
    </button>
    <button class="p-1.5" aria-label="Options">
      <EllipsisVerticalIcon size={20} />
    </button>
  </div>
</nav>
