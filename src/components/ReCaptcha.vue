<template>
  <div ref="gRecaptcha" />
</template>

<script lang="ts">
import Vue from 'vue'
export default Vue.extend({
  name: 'ReCaptcha',
  props: {
    siteKey: {
      type: String,
      required: true
    }
  },
  data () {
    return {
      gCaptcha: null,
      loading: false
    }
  },
  beforeMount () {
    if (!(window as any).grecaptcha) {
      this.loading = true
      const recaptcha = document.createElement('script')
      recaptcha.setAttribute('src',
        'https://www.google.com/recaptcha/api.js?&render=explicit'
      )
      document.head.appendChild(recaptcha)
      recaptcha.addEventListener('load', () => {
        setTimeout(() => {
          this.gCaptchaRender()
          this.loading = false
        }, 500)
      })
    }
  },
  mounted () {
    if ((window as any).grecaptcha && !this.loading && !this.gCaptcha) {
      this.gCaptchaRender()
    }
  },
  methods: {
    gCaptchaRender () {
      this.gCaptcha = (window as any).grecaptcha.render(
        this.$refs.gRecaptcha,
        {
          sitekey: this.siteKey,
          callback: (response: any) => this.$emit('verify', response),
          'expired-callback': () => this.$emit('expire'),
          'error-callback': () => this.$emit('fail'),
          size: 'invisible'
        }
      )
    },
    reset () {
      (window as any).grecaptcha.reset(this.gCaptcha)
    },
    execute () {
      (window as any).grecaptcha.execute(this.gCaptcha)
    }
  }
})
</script>
