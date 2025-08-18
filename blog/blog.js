(function(){
  const PAGE_SIZE = 6;
  const postsEl = document.getElementById('posts');
  const paginationEl = document.getElementById('pagination');
  const searchEl = document.getElementById('search');
  const categoryEl = document.getElementById('category');
  const tagsEl = document.getElementById('tags');

  let allPosts = [];
  let filtered = [];

  function getParams(){
    const url = new URL(window.location.href);
    return {
      page: parseInt(url.searchParams.get('page')||'1',10),
      q: url.searchParams.get('q')||'',
      tag: url.searchParams.get('tag')||'',
      category: url.searchParams.get('category')||''
    };
  }

  function setParams(params){
    const url = new URL(window.location.href);
    Object.entries(params).forEach(([k,v])=>{
      if (v) url.searchParams.set(k, v);
      else url.searchParams.delete(k);
    });
    history.replaceState({}, '', url);
  }

  function applyFilters(){
    const { q, tag, category } = getParams();
    filtered = allPosts.filter(p => {
      const matchesQ = q ? (p.title.toLowerCase().includes(q.toLowerCase()) || p.description.toLowerCase().includes(q.toLowerCase())) : true;
      const matchesTag = tag ? (p.tags || []).map(t=>t.toLowerCase()).includes(tag.toLowerCase()) : true;
      const matchesCategory = category ? (p.category||'').toLowerCase() === category.toLowerCase() : true;
      return matchesQ && matchesTag && matchesCategory;
    });
  }

  function renderTags(){
    const tags = new Set();
    allPosts.forEach(p => (p.tags||[]).forEach(t=>tags.add(t)));
    tagsEl.innerHTML = Array.from(tags).sort().map(t => 
      '<button class="skill-tag" data-tag="'+t+'">'+t+'</button>'
    ).join('');
    tagsEl.addEventListener('click', (e)=>{
      const btn = e.target.closest('button[data-tag]');
      if (!btn) return;
      setParams({ tag: btn.dataset.tag, page: 1 });
      searchEl.value = '';
      categoryEl.value = '';
      update();
    });
  }

  function renderCategories(){
    const cats = new Set(['']);
    allPosts.forEach(p => { if (p.category) cats.add(p.category); });
    categoryEl.innerHTML = '<option value="">All Categories</option>' + Array.from(cats).filter(Boolean).sort().map(c => '<option>'+c+'</option>').join('');
    const { category } = getParams();
    categoryEl.value = category;
  }

  function renderPage(){
    const { page } = getParams();
    const start = (page-1)*PAGE_SIZE;
    const pagePosts = filtered.slice(start, start+PAGE_SIZE);
    postsEl.innerHTML = pagePosts.map(p => `
      <article class="blog-card">
        <div class="blog-image">${p.cover ? '<img src="'+p.cover+'" alt="'+p.title+'" style="width:100%;height:100%;object-fit:cover;">' : '<i class="fas fa-file-alt"></i>'}</div>
        <div class="blog-content">
          <div class="blog-meta"><span class="blog-date">${p.prettyDate}</span>${p.category ? '<span class="blog-category">'+p.category+'</span>' : ''}</div>
          <h3>${p.title}</h3>
          <p>${p.description}</p>
          <a href="${p.url}" class="read-more">Read More →</a>
        </div>
      </article>
    `).join('');

    const totalPages = Math.max(1, Math.ceil(filtered.length / PAGE_SIZE));
    const curr = Math.min(Math.max(1, page), totalPages);
    let html = '';
    function btn(p, label){ return '<button class="btn btn-secondary" data-page="'+p+'" '+(p===curr?'disabled':'')+'>'+label+'</button>'; }
    html += btn(curr-1, 'Prev');
    for (let i=1;i<=totalPages;i++) html += btn(i, String(i));
    html += btn(curr+1, 'Next');
    paginationEl.innerHTML = html;
  }

  function update(){
    applyFilters();
    const totalPages = Math.max(1, Math.ceil(filtered.length / PAGE_SIZE));
    const current = Math.min(Math.max(1, getParams().page), totalPages);
    setParams({ page: current });
    renderPage();
  }

  function initEvents(){
    paginationEl.addEventListener('click', (e)=>{
      const btn = e.target.closest('button[data-page]');
      if (!btn) return;
      const p = parseInt(btn.dataset.page,10);
      setParams({ page: p });
      renderPage();
    });
    searchEl.addEventListener('input', ()=>{
      setParams({ q: searchEl.value, page: 1, tag: '' });
      categoryEl.value = '';
      update();
    });
    categoryEl.addEventListener('change', ()=>{
      setParams({ category: categoryEl.value, page: 1, tag: '', q: '' });
      searchEl.value = '';
      update();
    });
  }

  fetch('/assets/posts.json')
    .then(r=>r.json())
    .then(posts => {
      allPosts = posts;
      renderTags();
      renderCategories();
      const { q, tag } = getParams();
      if (q) searchEl.value = q;
      if (tag) setParams({ tag });
      initEvents();
      update();
    })
    .catch(err => {
      console.error('Failed to load posts.json', err);
      postsEl.innerHTML = '<p>Failed to load posts.</p>';
    });
})();


