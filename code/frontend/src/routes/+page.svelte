<script lang="ts">
	import { Tabs } from '@skeletonlabs/skeleton-svelte';
	import { Progress } from '@skeletonlabs/skeleton-svelte';
    import { onMount } from 'svelte';

    let task_name = "";
    let task_content = ""

    let tasks:any = [];

    onMount(async () => {
        const res = await fetch("http://127.0.0.1:5000/api/get_tasks");
        tasks = await res.json();
    })
    const refresh = async() => {
        const res = await fetch("http://127.0.0.1:5000/api/get_tasks");
        tasks = await res.json();
    }
    
    const create_task = async() => {
        const res = await fetch('http://127.0.0.1:5000/api/create_task',{
            method : 'POST',
            headers: {'content-type':'application/json'},
            body: JSON.stringify({
                taskName : task_name,
                taskContent : task_content
            })
        });
        const newTask = await res.json()
        console.log("TASK CREATED:",newTask)
    }

    



</script>

<div class="flex p-2 gap-2 ">
    <div class="container p-5 h-full w-1/2 border-2 border-solid border-primary-950 rounded-lg">
        <h2 class="text-center text-primary-500 text-5xl">Tasks</h2>
        <hr class="hr my-2">
        <Tabs defaultValue="{tasks[0]?.taskName || ''}" orientation="vertical" class="">
            <Tabs.List>
                {#each tasks as task }
                
                    <Tabs.Trigger value={task.taskName} class="justify-start">{task.taskName}</Tabs.Trigger>
                    
                {/each}
                <Tabs.Indicator />
            </Tabs.List>
            {#each tasks as task }
                    <Tabs.Content value={task.taskName}>  
                                {task.taskContent}
                    </Tabs.Content>       
            {/each}
    
    </Tabs>
   
    </div>
    <div class="container p-5 h-full w-1/2 border-2 border-solid border-primary-950 rounded-lg">
        <h2 class="text-center text-primary-500 text-5xl">Add a task</h2>
      
        <hr class="hr my-2">
        <small>task name:</small>
        <input type="text" class="border-primary-500 border-solid" bind:value={task_name}>
        <hr class="hr my-2">    
        <small>task content:</small>
        <input type="text" class="border-primary-500 border-solid" bind:value={task_content}>
        <hr class="hr my-2">
        <button type="button" on:click={create_task} class="btn preset-filled-primary-500">submit</button>

    </div>
    <button type="button" on:click={refresh} class="btn preset-filled-primary-500 ">Refresh</button>

</div>