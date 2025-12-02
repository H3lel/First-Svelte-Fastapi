<script lang="ts">
	import { Tabs } from '@skeletonlabs/skeleton-svelte';
	import { Progress } from '@skeletonlabs/skeleton-svelte';

    let new_task = "";
    let tasks:any = [
        {"id":1,"name":"labor","content":"clean your house","prog":74},
        {"id":2,"name":"wash the dishes","content":"clean your sink","prog":45},

        ];
</script>
<div class="flex p-2 gap-2">
    <div class="container p-5 h-full w-1/2 border-2 border-solid border-primary-950 rounded-lg">
        <h2 class="text-center text-primary-500 text-5xl">Tasks</h2>
        <hr class="hr my-2">
        <Tabs defaultValue="{tasks[1].name}" orientation="vertical" class="">
            <Tabs.List>
                {#each tasks as task }
                
                    <Tabs.Trigger value={task.name} class="justify-start">{task.name}</Tabs.Trigger>
                    
                {/each}
                <Tabs.Indicator />
            </Tabs.List>
            {#each tasks as task }
                    <Tabs.Content value={task.name}>  
                                {task.content}
                    </Tabs.Content>       
            {/each}
    
    </Tabs>
   
    </div>
    <div class="container p-5 h-full w-1/2 border-2 border-solid border-primary-950 rounded-lg">
        <h2 class="text-center text-primary-500 text-5xl">Add a task</h2>
        <p class="text-center text-primary-500">{new_task}</p>
        <hr class="hr my-2">
        <small>task name:</small>
        <input type="text"  bind:value={new_task}>

    </div>
</div>