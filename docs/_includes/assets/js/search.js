(function (jtd, undefined) {

// Event listener for search input
var initSearch = function() {
  var searchInput = document.getElementById('search-input');
  var searchResults = document.getElementById('search-results');
  var currentInput;
  var currentSearchIndex = 0;

  var index = lunr(function () {
    this.ref('id');
    this.field('title', { boost: 20 });
    this.field('content', { boost: 10 });
    this.field('url');
  });

  jtd.addEvent(searchInput, 'keyup', function (e) {
    var query = searchInput.value;
    if (query === currentInput) {
      return;
    }
    currentInput = query;
    searchResults.innerHTML = '';
    if (query === '') {
      return;
    }

    var results = index.search(query);

    if (results.length > 0) {
      currentSearchIndex = 0;
      var resultsHTML = '';
      results.forEach(function (result) {
        var item = window.data[result.ref];
        var title = item.title;
        var content = item.content.substring(0, 150);
        resultsHTML += `
          <div class="search-result">
            <a href="${item.url}" class="search-result-title">${title}</a>
            <div class="search-result-content">${content}...</div>
          </div>`;
      });
      searchResults.innerHTML = resultsHTML;
    } else {
      searchResults.innerHTML = '<p class="search-no-results">No results found</p>';
    }
  });

  // Handle keyboard navigation
  jtd.addEvent(searchInput, 'keydown', function(e) {
    switch (e.key) {
      case 'ArrowDown':
        e.preventDefault();
        var results = document.getElementsByClassName('search-result');
        if (currentSearchIndex < results.length - 1) {
          currentSearchIndex++;
          results[currentSearchIndex].focus();
        }
        break;
      case 'ArrowUp':
        e.preventDefault();
        var results = document.getElementsByClassName('search-result');
        if (currentSearchIndex > 0) {
          currentSearchIndex--;
          results[currentSearchIndex].focus();
        }
        break;
      case 'Enter':
        e.preventDefault();
        var results = document.getElementsByClassName('search-result');
        if (results.length > 0 && currentSearchIndex >= 0) {
          results[currentSearchIndex].querySelector('a').click();
        }
        break;
    }
  });

  // Initialize search data
  var pages = document.getElementsByClassName('page');
  Array.prototype.forEach.call(pages, function(page) {
    var url = page.id;
    var title = page.querySelector('.page-title').textContent;
    var content = page.querySelector('.main-content').textContent;
    index.add({
      id: url,
      title: title,
      content: content,
      url: url
    });
  });
};

// Export search functionality
jtd.initSearch = initSearch;

})(window.jtd = window.jtd || {});
