import { promises as fs } from 'fs';
import path from 'path';
import matter from 'gray-matter';
import { marked } from 'marked';
import { globSync } from 'glob';

const __dirname = path.resolve();

// ---------- Config ----------
const SITE_URL = process.env.SITE_URL || 'https://mohithnovoct.github.io';
const SITE_TITLE = 'Mohith Butta';
const SITE_DESC = 'Python Programmer & AI Enthusiast';
const POSTS_DIR = path.join(__dirname, 'posts');
const OUTPUT_DIR = path.join(__dirname, 'blog');
const ASSETS_DIR = path.join(__dirname, 'assets');
const POSTS_JSON = path.join(ASSETS_DIR, 'posts.json');

// Giscus (comments) - ensure your repo is configured with Giscus
const GISCUS = {
	repo: 'mohithnovoct/mohithnovoct.github.io',
	repoId: '', // optional: fill to avoid runtime network lookup
	category: 'General',
	categoryId: '', // optional
	mapping: 'pathname',
	reactionsEnabled: '1',
	emitMetadata: '0',
	inputPosition: 'bottom',
	theme: 'light',
	lang: 'en'
};

// ---------- Helpers ----------
function slugify(input) {
	return String(input)
		.toLowerCase()
		.trim()
		.replace(/[^a-z0-9\s-]/g, '')
		.replace(/\s+/g, '-')
		.replace(/-+/g, '-');
}

function toExcerpt(html, maxLength = 180) {
	const text = html
		.replace(/<script[\s\S]*?<\/script>/gi, '')
		.replace(/<style[\s\S]*?<\/style>/gi, '')
		.replace(/<[^>]*>/g, '')
		.replace(/\s+/g, ' ')
		.trim();
	if (text.length <= maxLength) return text;
	return text.slice(0, maxLength).trim() + '…';
}

function formatDateISO(date) {
	const d = new Date(date);
	if (isNaN(d.getTime())) return new Date().toISOString();
	return d.toISOString();
}

function formatDatePretty(date) {
	const d = new Date(date);
	return d.toLocaleDateString('en-US', { year: 'numeric', month: 'long', day: 'numeric' });
}

async function ensureDir(dir) {
	await fs.mkdir(dir, { recursive: true });
}

// ---------- Templates ----------
function renderPostHTML({ title, description, dateISO, datePretty, tags, category, html, url, cover }) {
	const tagsMeta = Array.isArray(tags) ? tags.join(', ') : '';
	const jsonLd = {
		'@context': 'https://schema.org',
		'@type': 'BlogPosting',
		headline: title,
		description,
		datePublished: dateISO,
		dateModified: dateISO,
		author: { '@type': 'Person', name: SITE_TITLE },
		mainEntityOfPage: url,
		image: cover || undefined
	};

	return `<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<title>${title} — ${SITE_TITLE}</title>
	<meta name="description" content="${escapeHtml(description)}">
	<link rel="stylesheet" href="/styles.css">
	<link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css" rel="stylesheet">
	<link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">
	<link rel="canonical" href="${url}">
	<meta property="og:type" content="article">
	<meta property="og:title" content="${escapeHtml(title)}">
	<meta property="og:description" content="${escapeHtml(description)}">
	<meta property="og:url" content="${url}">
	${cover ? `<meta property="og:image" content="${cover}">` : ''}
	<meta name="twitter:card" content="summary_large_image">
	<meta name="twitter:title" content="${escapeHtml(title)}">
	<meta name="twitter:description" content="${escapeHtml(description)}">
	${cover ? `<meta name="twitter:image" content="${cover}">` : ''}
	<script type="application/ld+json">${JSON.stringify(jsonLd)}</script>
</head>
<body>
	<nav class="navbar">
		<div class="nav-container">
			<div class="nav-logo"><h2>${SITE_TITLE}</h2></div>
			<ul class="nav-menu">
				<li><a href="/index.html#home" class="nav-link">Home</a></li>
				<li><a href="/index.html#about" class="nav-link">About</a></li>
				<li><a href="/index.html#projects" class="nav-link">Projects</a></li>
				<li><a href="/blog/" class="nav-link">Blog</a></li>
				<li><a href="/index.html#contact" class="nav-link">Contact</a></li>
			</ul>
			<div class="nav-toggle">
				<button id="theme-toggle" class="theme-btn"><i class="fas fa-moon"></i></button>
				<div class="hamburger"><span></span><span></span><span></span></div>
			</div>
		</div>
	</nav>

	<main style="padding-top:120px">
		<article class="container" style="max-width: 800px;">
			<header style="margin-bottom: 2rem;">
				<h1 class="section-title" style="text-align:left; margin-bottom:0.5rem;">${escapeHtml(title)}</h1>
				<div class="blog-meta"><span class="blog-date">${datePretty}</span>${category ? `<span class="blog-category">${escapeHtml(category)}</span>` : ''}</div>
				${cover ? `<img src="${cover}" alt="${escapeHtml(title)}" style="width:100%;border-radius:12px;margin:1rem 0;">` : ''}
				${tags && tags.length ? `<div class="skill-tags">${tags.map(t => `<span class='skill-tag'>${escapeHtml(t)}</span>`).join('')}</div>` : ''}
			</header>
			<div class="post-content">${html}</div>
			<section id="comments" style="margin-top:3rem;">
				<script src="https://giscus.app/client.js"
					data-repo="${GISCUS.repo}"
					${GISCUS.repoId ? `data-repo-id="${GISCUS.repoId}"` : ''}
					data-category="${GISCUS.category}"
					${GISCUS.categoryId ? `data-category-id="${GISCUS.categoryId}"` : ''}
					data-mapping="${GISCUS.mapping}"
					data-reactions-enabled="${GISCUS.reactionsEnabled}"
					data-emit-metadata="${GISCUS.emitMetadata}"
					data-input-position="${GISCUS.inputPosition}"
					data-theme="${GISCUS.theme}"
					data-lang="${GISCUS.lang}"
					crossorigin="anonymous"
					async>
				</script>
			</section>
		</article>
	</main>
	<script src="/script.js"></script>
</body>
</html>`;
}

function renderBlogIndexHTML() {
	return `<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<title>Blog — ${SITE_TITLE}</title>
	<meta name="description" content="Blog posts by ${SITE_TITLE}. ${SITE_DESC}">
	<link rel="stylesheet" href="/styles.css">
	<link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css" rel="stylesheet">
	<link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">
	<link rel="canonical" href="${SITE_URL}/blog/">
</head>
<body>
	<nav class="navbar">
		<div class="nav-container">
			<div class="nav-logo"><h2>${SITE_TITLE}</h2></div>
			<ul class="nav-menu">
				<li><a href="/index.html#home" class="nav-link">Home</a></li>
				<li><a href="/index.html#about" class="nav-link">About</a></li>
				<li><a href="/index.html#projects" class="nav-link">Projects</a></li>
				<li><a href="/blog/" class="nav-link">Blog</a></li>
				<li><a href="/index.html#contact" class="nav-link">Contact</a></li>
			</ul>
			<div class="nav-toggle">
				<button id="theme-toggle" class="theme-btn"><i class="fas fa-moon"></i></button>
				<div class="hamburger"><span></span><span></span><span></span></div>
			</div>
		</div>
	</nav>

	<main style="padding-top:120px">
		<section class="blog">
			<div class="container">
				<h2 class="section-title">Blog</h2>
				<div class="filters" style="display:flex;gap:1rem;flex-wrap:wrap;margin-bottom:1rem;">
					<input id="search" type="search" placeholder="Search posts..." style="flex:1;min-width:240px;padding:0.75rem;border-radius:8px;border:1px solid var(--border-color);">
					<select id="category" style="padding:0.75rem;border-radius:8px;border:1px solid var(--border-color);min-width:180px;">
						<option value="">All Categories</option>
					</select>
				</div>
				<div id="tags" class="skill-tags" style="margin-bottom:1rem;"></div>
				<div id="posts" class="blog-grid"></div>
				<div id="pagination" style="display:flex;gap:0.5rem;justify-content:center;margin-top:2rem;"></div>
			</div>
		</section>
	</main>
	<script src="/script.js"></script>
	<script src="/blog/blog.js"></script>
</body>
</html>`;
}

function escapeHtml(str = '') {
	return String(str)
		.replace(/&/g, '&amp;')
		.replace(/</g, '&lt;')
		.replace(/>/g, '&gt;')
		.replace(/"/g, '&quot;')
		.replace(/'/g, '&#039;');
}

// ---------- Build Steps ----------
async function readPosts() {
	await ensureDir(POSTS_DIR);
	const files = globSync('*.md', { cwd: POSTS_DIR, nodir: true });
	const posts = [];
	for (const file of files) {
		const fullPath = path.join(POSTS_DIR, file);
		const raw = await fs.readFile(fullPath, 'utf8');
		const { content, data } = matter(raw);
		if (data.draft) continue;
		const title = data.title || path.parse(file).name;
		const slug = data.slug ? slugify(data.slug) : slugify(path.parse(file).name);
		const stat = await fs.stat(fullPath);
		const dateISO = formatDateISO(data.date || stat.mtime.toISOString());
		const datePretty = formatDatePretty(dateISO);
		const html = marked.parse(content);
		const description = data.description || toExcerpt(html);
		const url = `${SITE_URL}/blog/${slug}/`;
		const post = {
			title,
			slug,
			dateISO,
			datePretty,
			tags: Array.isArray(data.tags) ? data.tags : (data.tags ? String(data.tags).split(',').map(s => s.trim()).filter(Boolean) : []),
			category: data.category || '',
			description,
			cover: data.cover || '',
			html,
			url
		};
		posts.push(post);
	}
	// newest first
	posts.sort((a, b) => new Date(b.dateISO) - new Date(a.dateISO));
	return posts;
}

async function writePostsJson(posts) {
	await ensureDir(ASSETS_DIR);
	const minimal = posts.map(p => ({
		title: p.title,
		slug: p.slug,
		date: p.dateISO,
		prettyDate: p.datePretty,
		tags: p.tags,
		category: p.category,
		description: p.description,
		cover: p.cover,
		url: p.url
	}));
	await fs.writeFile(POSTS_JSON, JSON.stringify(minimal, null, 2), 'utf8');
}

async function writePostPages(posts) {
	for (const p of posts) {
		const dir = path.join(OUTPUT_DIR, p.slug);
		await ensureDir(dir);
		const html = renderPostHTML(p);
		await fs.writeFile(path.join(dir, 'index.html'), html, 'utf8');
	}
}

async function writeBlogIndex() {
	await ensureDir(OUTPUT_DIR);
	await fs.writeFile(path.join(OUTPUT_DIR, 'index.html'), renderBlogIndexHTML(), 'utf8');
}

async function writeSitemap(posts) {
	const latestDateISO = posts.length ? posts.reduce((acc, p) => new Date(p.dateISO) > new Date(acc) ? p.dateISO : acc, posts[0].dateISO) : new Date(0).toISOString();
	const entries = [
		{ loc: `${SITE_URL}/`, lastmod: latestDateISO, changefreq: 'weekly', priority: '1.0' },
		{ loc: `${SITE_URL}/blog/`, lastmod: latestDateISO, changefreq: 'weekly', priority: '0.8' },
		...posts.map(p => ({ loc: p.url, lastmod: p.dateISO, changefreq: 'monthly', priority: '0.6' }))
	];
	const xml = `<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
${entries.map(e => `  <url>\n    <loc>${e.loc}</loc>\n    <lastmod>${e.lastmod}</lastmod>\n    <changefreq>${e.changefreq}</changefreq>\n    <priority>${e.priority}</priority>\n  </url>`).join('\n')}
</urlset>`;
	await fs.writeFile(path.join(__dirname, 'sitemap.xml'), xml, 'utf8');
}

async function writeRSS(posts) {
	const items = posts
		.map((p) => `
    <item>
      <title>${escapeHtml(p.title)}</title>
      <link>${p.url}</link>
      <guid>${p.url}</guid>
      <pubDate>${new Date(p.dateISO).toUTCString()}</pubDate>
      <description>${escapeHtml(p.description)}</description>
    </item>`)
		.join('\n');
	const xml = `<?xml version="1.0" encoding="UTF-8"?>
<rss version="2.0">
  <channel>
    <title>${SITE_TITLE} — Blog</title>
    <link>${SITE_URL}/blog/</link>
    <description>${SITE_DESC}</description>
${items}
  </channel>
</rss>`;
	await fs.writeFile(path.join(__dirname, 'feed.xml'), xml, 'utf8');
}

async function writeBlogJS() {
	const src = path.join(__dirname, 'blog', 'blog.js');
	try {
		const content = await fs.readFile(src, 'utf8');
		await ensureDir(OUTPUT_DIR);
		await fs.writeFile(path.join(OUTPUT_DIR, 'blog.js'), content, 'utf8');
	} catch (e) {
		// no-op if source not found
	}
}

// ---------- Main ----------
async function main() {
	const posts = await readPosts();
	await writePostsJson(posts);
	await writePostPages(posts);
	await writeBlogIndex();
	await writeBlogJS();
	await writeSitemap(posts);
	await writeRSS(posts);
	console.log(`Built ${posts.length} posts.`);
}

main().catch((err) => {
	console.error(err);
	process.exit(1);
});


