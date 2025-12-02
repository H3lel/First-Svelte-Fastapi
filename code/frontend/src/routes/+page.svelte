<script lang="ts">
    
    var tasks:any = [
        {"id":1,"name":"labor1","description":"test1"},
        {"id":2,"name":"labor2","description":"test2"},
        {"id":3,"name":"labor3","description":"test3"},
    ];
    var user_in:string;
</script>


<h1>TODO APP</h1>
{#if tasks}
    <table>
        <thead>
            <tr>
                <th>Task Id</th>
                <th>Task name</th>
                <th>Description</th>
            </tr>
        </thead>
        <tbody>
            {#each tasks as task}
                <tr>
                    <td>{task.id}</td>
                    <td>{task.name}</td>
                    <td>{task.description}</td>


                </tr>
            {/each}
        </tbody>
    </table>
{:else}
    <h1>There is no task</h1>
{/if}


<p>task name {user_in}</p>
<input type="text" bind:value={user_in} class="border-2 border-solid">

