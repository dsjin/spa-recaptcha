<template>
  <div>
    <re-captcha
      :siteKey="''"
      @verify="verify"
      @expired-callback="expiredCallback"
      @error-callback="errorCallback"
      ref="recaptcha"
    />
    <button
      @click="invoke"
    >
      Invoke The Challenge
    </button>
    <button
      @click="getToken"
    >
      Get Token
    </button>
    {{ token }}
  </div>
</template>

<script lang="ts">
import Vue from 'vue'
import ReCaptcha from '@/components/ReCaptcha.vue'
export default Vue.extend({
  name: 'SendForm',
  components: {
    ReCaptcha
  },
  data () {
    return {
      token: ''
    }
  },
  methods: {
    verify (response: any) {
      console.log(response)
    },
    expiredCallback () {
      console.log('expiredCallback')
    },
    errorCallback () {
      console.log('errorCallback')
    },
    invoke () {
      (this.$refs.recaptcha as any).execute()
    },
    getToken () {
      this.token = (this.$refs.recaptcha as any).token()
      if (!this.token) {
        this.token = 'Please challenge once agian'
      }
    }
  }
})
</script>

<style>
</style>
