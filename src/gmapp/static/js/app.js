const popoverTriggerList = document.querySelectorAll('[data-bs-toggle="popover"]');


// NOTE: To use HTML in the popover content, you need to set the `data-html-content` attribute on the element.
const popoverList = [...popoverTriggerList].map(popoverTriggerEl => {
  const htmlContent = popoverTriggerEl.getAttribute('data-html-content');

  return new bootstrap.Popover(popoverTriggerEl, {
    content: htmlContent,
    html: true,
    sanitize: false 
  });
});

// general js request code

// General function for making AJAX requests using fetch
async function makeRequest(url, method = 'GET', data = null, headers = {}) {
    const defaultHeaders = {
        'Content-Type': 'application/json',
        'X-Requested-With': 'XMLHttpRequest',
    };
    // Add CSRF token for Django
    const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]');
    if (csrfToken) {
        defaultHeaders['X-CSRFToken'] = csrfToken.value;
    }
    const allHeaders = { ...defaultHeaders, ...headers };

    const options = {
        method,
        headers: allHeaders,
    };
    if (data && method !== 'GET') {
        options.body = JSON.stringify(data);
    }
    try {
        const response = await fetch(url, options);
        const contentType = response.headers.get('content-type');
        let responseData;
        if (contentType && contentType.includes('application/json')) {
            responseData = await response.json();
        } else {
            responseData = await response.text();
        }
        if (!response.ok) {
            throw {
                status: response.status,
                statusText: response.statusText,
                response: responseData
            };
        }
        return responseData;
    } catch (error) {
        throw error;
    }
}

// Helper functions for common HTTP methods
const api = {
    get: (url, headers = {}) => makeRequest(url, 'GET', null, headers),
    post: (url, data, headers = {}) => makeRequest(url, 'POST', data, headers)
};
